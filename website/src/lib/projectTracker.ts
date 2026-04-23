const statusLoaders = import.meta.glob('../../../Formalization/STATUS.md');
const openProblemLoaders = import.meta.glob('../../../Formalization/OPEN_PROBLEMS.md');

type MarkdownModule = {
	rawContent: () => string;
};

type MarkdownLoader = () => Promise<MarkdownModule>;

export type ActiveFront = {
	index: number;
	title: string;
	summary: string;
	priority: string | null;
};

export type OpenProblem = {
	id: string;
	title: string;
	statement: string;
	status: string;
};

export type ProjectTrackerSnapshot = {
	lastUpdated: string;
	activePaperPath: string;
	activePaperMasthead: string;
	activePaperVersion: string;
	activeFronts: ActiveFront[];
	openProblems: OpenProblem[];
	recentChanges: { date: string; title: string }[];
	activeFrontCount: number;
	openProblemCount: number;
};

function collapseWhitespace(value: string) {
	return value.replace(/\s+/g, ' ').trim();
}

function escapeRegExp(value: string) {
	return value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function truncate(value: string, maxLength: number) {
	if (value.length <= maxLength) {
		return value;
	}

	return `${value.slice(0, maxLength - 1).trimEnd()}…`;
}

function normalizeTitle(value: string) {
	return collapseWhitespace(value).replace(/\.$/, '');
}

function getSectionBody(raw: string, heading: string) {
	const headingPattern = new RegExp(`^## ${escapeRegExp(heading)}\\s*$`, 'm');
	const startIndex = raw.search(headingPattern);

	if (startIndex === -1) {
		return '';
	}

	const sectionStart = raw.indexOf('\n', startIndex);
	const remainder = raw.slice(sectionStart + 1);
	const nextHeading = remainder.match(/^##\s+/m);

	return (nextHeading ? remainder.slice(0, nextHeading.index) : remainder).trim();
}

async function loadSingleRawDocument(loaders: Record<string, MarkdownLoader>) {
	const [loader] = Object.values(loaders) as MarkdownLoader[];

	if (!loader) {
		throw new Error('Expected exactly one tracker document loader.');
	}

	const module = await loader();
	return module.rawContent();
}

function parseStatusMetadata(raw: string) {
	const lastUpdatedMatch = raw.match(/^\*\*Last updated:\*\*\s+(.+)$/m);
	const activePaperMatch = raw.match(
		/^\*\*Active paper:\*\*\s+`([^`]+)`(?:\s+\(internal masthead:\s+"([^"]+)"\))?$/m,
	);

	const activePaperPath = activePaperMatch?.[1] ?? '';
	const activePaperMasthead = activePaperMatch?.[2] ?? '';
	const activePaperVersion =
		activePaperMasthead.match(/\bv[\d.]+\b/i)?.[0] ??
		activePaperPath.match(/\bv[\d.]+\b/i)?.[0] ??
		'Live';

	return {
		lastUpdated: lastUpdatedMatch?.[1]?.trim() ?? 'Unknown',
		activePaperPath,
		activePaperMasthead,
		activePaperVersion,
	};
}

function parseActiveFronts(raw: string): ActiveFront[] {
	const section = getSectionBody(raw, 'Active fronts');
	const lines = section
		.split('\n')
		.map((line) => line.trim())
		.filter((line) => line.startsWith('**'));

	return lines.map((line) => {
		const match = line.match(/^\*\*(\d+)\.\s+([\s\S]+?)\*\*\s+([\s\S]+)$/);

		if (!match) {
			throw new Error(`Unable to parse active front line: ${line}`);
		}

		const index = Number(match[1]);
		const title = normalizeTitle(match[2]);
		const body = collapseWhitespace(match[3]);
		const priorityMatch = body.match(/\*\(Priority:\s*([\s\S]*?)\)\*$/);
		const summary = truncate(
			collapseWhitespace(body.replace(/\s*\*\(Priority:[\s\S]*?\)\*$/, '')),
			280,
		);

		return {
			index,
			title,
			summary,
			priority: priorityMatch?.[1]?.trim() ?? null,
		};
	});
}

function parseFieldLine(block: string, label: string) {
	const marker = `**${label}.**`;
	const line = block
		.split('\n')
		.map((entry) => entry.trim())
		.find((entry) => entry.startsWith(marker));

	return line ? line.slice(marker.length).trim() : '';
}

function parseOpenProblems(raw: string): OpenProblem[] {
	const section = getSectionBody(raw, 'Open');
	const blocks = section
		.split(/\n(?=###\s+)/)
		.map((block) => block.trim())
		.filter(Boolean);

	return blocks.map((block) => {
		const [headingLine] = block.split('\n');
		const match = headingLine.match(/^###\s+(OP-[A-Z0-9-]+)\s+—\s+(.+)$/);

		if (!match) {
			throw new Error(`Unable to parse open problem block: ${headingLine}`);
		}

		return {
			id: match[1],
			title: normalizeTitle(match[2]),
			statement: truncate(parseFieldLine(block, 'Statement'), 220),
			status: parseFieldLine(block, 'Status'),
		};
	});
}

function parseRecentChanges(raw: string) {
	const section = getSectionBody(raw, 'Changelog');

	return section
		.split('\n')
		.map((line) => line.trim())
		.filter((line) => line.startsWith('### '))
		.map((line) => {
			const match = line.match(/^###\s+(\d{4}-\d{2}-\d{2})\s+—\s+(.+)$/);

			return {
				date: match?.[1] ?? '',
				title: normalizeTitle(match?.[2] ?? line.replace(/^###\s+/, '')),
			};
		});
}

const snapshotPromise: Promise<ProjectTrackerSnapshot> = (async () => {
	const [statusRaw, openProblemsRaw] = await Promise.all([
		loadSingleRawDocument(statusLoaders as Record<string, MarkdownLoader>),
		loadSingleRawDocument(openProblemLoaders as Record<string, MarkdownLoader>),
	]);

	const metadata = parseStatusMetadata(statusRaw);
	const activeFronts = parseActiveFronts(statusRaw);
	const openProblems = parseOpenProblems(openProblemsRaw);
	const recentChanges = parseRecentChanges(statusRaw);

	return {
		...metadata,
		activeFronts,
		openProblems,
		recentChanges,
		activeFrontCount: activeFronts.length,
		openProblemCount: openProblems.length,
	};
})();

export async function getProjectTrackerSnapshot() {
	return snapshotPromise;
}
