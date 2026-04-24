const sectionConfigs = {
	project: {
		label: 'Project Docs',
		description: 'Root documents that explain the live state of the research program.',
	},
	paper: {
		label: 'Paper',
		description: 'The active manuscript and core public-facing theory spine.',
	},
	proofs: {
		label: 'Proofs',
		description: 'Standalone theorem documents and derivations supporting the main paper.',
	},
	reductions: {
		label: 'Reductions',
		description: 'Cross-domain reductions showing other frameworks as special cases.',
	},
	bridges: {
		label: 'Bridges',
		description: 'Structural bridge documents linking the theory to adjacent formalisms.',
	},
	research: {
		label: 'Research',
		description: 'Literature surveys, synthesis notes, and supporting research integrations.',
	},
	simulations: {
		label: 'Simulations',
		description: 'Empirical tooling notes and simulation-facing experiment documentation.',
	},
	essays: {
		label: 'Essays',
		description: 'Philosophical and interpretive companion writing.',
	},
	laws: {
		label: 'Laws',
		description: 'Flagship law documents and broader structural-law formulations.',
	},
	audits: {
		label: 'Audits',
		description: 'Integrity and packaging reviews of the manuscript state.',
	},
	sessions: {
		label: 'Sessions',
		description: 'Session-by-session research notes and change logs.',
	},
} as const;

const moduleLoaders = {
	project: import.meta.glob('../../../Formalization/{README,STATUS,OPEN_PROBLEMS}.md'),
	paper: import.meta.glob('../../../Formalization/paper/*.md'),
	proofs: import.meta.glob('../../../Formalization/proofs/*.md'),
	reductions: import.meta.glob('../../../Formalization/reductions/*.md'),
	bridges: import.meta.glob('../../../Formalization/bridges/*.md'),
	research: import.meta.glob('../../../Formalization/research/*.md'),
	simulations: import.meta.glob('../../../Formalization/simulations/*.md'),
	essays: import.meta.glob('../../../Formalization/essays/*.md'),
	laws: import.meta.glob('../../../Formalization/special_cases/*.md'),
	audits: import.meta.glob('../../../Formalization/audits/*.md'),
	sessions: import.meta.glob('../../../Formalization/sessions/*.md'),
} as const;

export type LibrarySection = keyof typeof sectionConfigs;

type Heading = {
	depth: number;
	slug: string;
	text: string;
};

type MarkdownModule = {
	Content: unknown;
	getHeadings: () => Heading[];
	rawContent: () => string;
};

export type LibraryEntry = {
	section: LibrarySection;
	sectionLabel: string;
	sectionDescription: string;
	slug: string;
	title: string;
	summary: string;
	path: string;
	sourcePath: string;
	load: () => Promise<MarkdownModule>;
};

function cleanInlineMarkdown(value: string) {
	return value
		.replace(/`([^`]+)`/g, '$1')
		.replace(/\*\*([^*]+)\*\*/g, '$1')
		.replace(/\*([^*]+)\*/g, '$1')
		.replace(/^\#+\s*/, '')
		.trim();
}

function titleFromRaw(raw: string, fallback: string) {
	const firstMeaningfulLine = raw
		.split('\n')
		.map((line) => line.trim())
		.find((line) => line.length > 0);

	if (!firstMeaningfulLine) {
		return fallback;
	}

	if (/^#\s+/.test(firstMeaningfulLine)) {
		return cleanInlineMarkdown(firstMeaningfulLine);
	}

	if (/^\*\*.+\*\*$/.test(firstMeaningfulLine)) {
		return cleanInlineMarkdown(firstMeaningfulLine);
	}

	return fallback;
}

function summaryFromRaw(raw: string) {
	const lines = raw
		.split('\n')
		.map((line) => line.trim())
		.filter(Boolean)
		.filter((line) => !/^#{1,6}\s+/.test(line))
		.filter((line) => !/^\*\*.+\*\*$/.test(line))
		.filter((line) => !/^\*.+\*$/.test(line))
		.filter((line) => !/^[-*]\s+/.test(line))
		.filter((line) => !/^\|.+\|$/.test(line));

	const candidate = lines.find((line) => line.length > 48) ?? lines[0] ?? '';
	return cleanInlineMarkdown(candidate).slice(0, 240);
}

function prettyFallbackTitle(section: LibrarySection, slug: string) {
	const specialTitles: Partial<Record<LibrarySection, Record<string, string>>> = {
		project: {
			readme: 'Workspace Overview',
			status: 'Current Status',
			'open-problems': 'Open Problems',
		},
	};

	const special = specialTitles[section]?.[slug];
	if (special) {
		return special;
	}

	return slug
		.replace(/_/g, ' ')
		.replace(/-/g, ' ')
		.replace(/\bv(\d+)\b/gi, 'v$1')
		.replace(/\b\w/g, (char) => char.toUpperCase());
}

function slugFromPath(path: string, section: LibrarySection) {
	const fileName = path.split('/').pop()?.replace(/\.md$/, '') ?? '';

	if (section === 'project') {
		if (fileName === 'README') return 'readme';
		if (fileName === 'STATUS') return 'status';
		if (fileName === 'OPEN_PROBLEMS') return 'open-problems';
	}

	return fileName
		.toLowerCase()
		.replace(/['’]/g, '')
		.replace(/[^a-z0-9_-]+/g, '-')
		.replace(/^-+|-+$/g, '');
}

const sectionOrder = Object.keys(sectionConfigs) as LibrarySection[];

const allEntriesPromise: Promise<LibraryEntry[]> = (async () => {
	const collected = await Promise.all(
		sectionOrder.flatMap((section) =>
			Object.entries(moduleLoaders[section]).map(async ([path, load]) => {
				const slug = slugFromPath(path, section);
				const rawModule = await load();
				const raw = rawModule.rawContent();
				const fallback = prettyFallbackTitle(section, slug);

				return {
					section,
					sectionLabel: sectionConfigs[section].label,
					sectionDescription: sectionConfigs[section].description,
					slug,
					title: titleFromRaw(raw, fallback),
					summary: summaryFromRaw(raw),
					path: `/library/${section}/${slug}`,
					sourcePath: path.replace(/^.*\/Formalization\//, 'Formalization/'),
					load,
				} satisfies LibraryEntry;
			}),
		),
	);

	return collected.sort((left, right) => {
		if (left.section !== right.section) {
			return sectionOrder.indexOf(left.section) - sectionOrder.indexOf(right.section);
		}

		if (left.section === 'sessions') {
			return right.slug.localeCompare(left.slug);
		}

		return left.title.localeCompare(right.title);
	});
})();

export async function getLibraryEntries() {
	return allEntriesPromise;
}

export async function getSectionEntries(section: LibrarySection) {
	const entries = await getLibraryEntries();
	return entries.filter((entry) => entry.section === section);
}

export async function getLibraryEntry(section: string, slug: string) {
	const entries = await getLibraryEntries();
	return entries.find((entry) => entry.section === section && entry.slug === slug);
}

export function getSectionConfig(section: LibrarySection) {
	return sectionConfigs[section];
}

export function getSectionList() {
	return sectionOrder.map((section) => ({
		key: section,
		...sectionConfigs[section],
	}));
}
