import { readdir, readFile } from 'node:fs/promises';
import path from 'node:path';

const collectionConfigs = {
	slidedecks: {
		label: 'Slide Decks',
		description: 'PDF-first decks, explainers, and whiteboard sessions.',
		publishingHint:
			'Add a PDF deck plus an optional cover image in each folder to publish it cleanly on the site.',
		recommendedNames: ['deck.pdf', 'cover.webp'],
	},
	storytelling: {
		label: 'Storytelling',
		description: 'Comics, narrative slide sequences, and visual explainers exported as images.',
		publishingHint:
			'Add exported slide images in sequence order and an optional deck PDF for download.',
		recommendedNames: ['slide-01.webp', 'slide-02.webp', 'cover.webp', 'deck.pdf'],
	},
} as const;

export type PresentationCollection = keyof typeof collectionConfigs;

type PresentationMeta = {
	title?: string;
	summary?: string;
	order?: number;
	featured?: boolean;
};

export type PresentationAsset = {
	href: string;
	name: string;
};

export type PresentationEntry = {
	collection: PresentationCollection;
	collectionLabel: string;
	collectionDescription: string;
	collectionPath: string;
	slug: string;
	title: string;
	summary: string;
	path: string;
	assetFolder: string;
	coverHref: string | null;
	pdfs: PresentationAsset[];
	slides: PresentationAsset[];
	hasAssets: boolean;
	featured: boolean;
	order: number;
	publishingHint: string;
	recommendedNames: string[];
};

export type PresentationCollectionSummary = {
	key: PresentationCollection;
	label: string;
	description: string;
	path: string;
	publishingHint: string;
	recommendedNames: string[];
	entries: PresentationEntry[];
	entryCount: number;
	assetReadyCount: number;
};

const presentationsRoot = path.resolve(process.cwd(), 'public/presentations');

function naturalCompare(left: string, right: string) {
	return left.localeCompare(right, undefined, {
		numeric: true,
		sensitivity: 'base',
	});
}

function prettyTitle(value: string) {
	return value
		.replace(/[_-]+/g, ' ')
		.replace(/\b\w/g, (char) => char.toUpperCase());
}

function encodePath(parts: string[]) {
	return `/${parts.map((part) => encodeURIComponent(part)).join('/')}`;
}

function isImageFile(name: string) {
	return /\.(avif|gif|jpe?g|png|svg|webp)$/i.test(name);
}

function isPdfFile(name: string) {
	return /\.pdf$/i.test(name);
}

function isCoverFile(name: string) {
	return /^cover\./i.test(name) || /(?:^|-)cover\./i.test(name);
}

async function safeReadDir(dir: string) {
	try {
		return await readdir(dir, { withFileTypes: true });
	} catch {
		return [];
	}
}

async function loadMeta(dir: string): Promise<PresentationMeta> {
	try {
		const raw = await readFile(path.join(dir, 'meta.json'), 'utf8');
		const parsed = JSON.parse(raw);

		if (!parsed || typeof parsed !== 'object') {
			return {};
		}

		return parsed as PresentationMeta;
	} catch {
		return {};
	}
}

function defaultSummary(
	collection: PresentationCollection,
	pdfCount: number,
	slideCount: number,
) {
	if (collection === 'slidedecks') {
		if (pdfCount > 0) {
			return pdfCount === 1
				? 'PDF deck ready for reading and embedding on the site.'
				: 'Multiple PDFs ready for deck browsing and direct download.';
		}

		return 'Scaffolded deck folder. Add a PDF and optional cover image to publish it.';
	}

	if (slideCount > 0) {
		return slideCount === 1
			? 'Single storytelling frame currently published.'
			: `Storytelling sequence with ${slideCount} published slides.`;
	}

	return 'Scaffolded storytelling folder. Add slide images in order to publish it.';
}

async function getCollectionEntries(
	collection: PresentationCollection,
): Promise<PresentationEntry[]> {
	const config = collectionConfigs[collection];
	const collectionDir = path.join(presentationsRoot, collection);
	const dirents = await safeReadDir(collectionDir);
	const slugs = dirents
		.filter((dirent) => dirent.isDirectory() && !dirent.name.startsWith('.'))
		.map((dirent) => dirent.name)
		.sort(naturalCompare);

	const entries = await Promise.all(
		slugs.map(async (slug) => {
			const entryDir = path.join(collectionDir, slug);
			const meta = await loadMeta(entryDir);
			const dirFiles = await safeReadDir(entryDir);
			const files = dirFiles
				.filter((dirent) => dirent.isFile() && !dirent.name.startsWith('.'))
				.map((dirent) => dirent.name)
				.filter((name) => name !== 'meta.json')
				.sort(naturalCompare);

			const imageFiles = files.filter(isImageFile);
			const coverFile = imageFiles.find(isCoverFile) ?? null;
			const slides = imageFiles
				.filter((name) => name !== coverFile)
				.map((name) => ({
					name,
					href: encodePath(['presentations', collection, slug, name]),
				}));
			const pdfs = files.filter(isPdfFile).map((name) => ({
				name,
				href: encodePath(['presentations', collection, slug, name]),
			}));
			const title = meta.title?.trim() || prettyTitle(slug);
			const summary =
				meta.summary?.trim() || defaultSummary(collection, pdfs.length, slides.length);
			const order = Number.isFinite(meta.order) ? Number(meta.order) : 999;
			const featured = meta.featured ?? false;

			return {
				collection,
				collectionLabel: config.label,
				collectionDescription: config.description,
				collectionPath: `/presentations/${collection}`,
				slug,
				title,
				summary,
				path: `/presentations/${collection}/${slug}`,
				assetFolder: `website/public/presentations/${collection}/${slug}/`,
				coverHref: coverFile
					? encodePath(['presentations', collection, slug, coverFile])
					: null,
				pdfs,
				slides,
				hasAssets: Boolean(coverFile) || pdfs.length > 0 || slides.length > 0,
				featured,
				order,
				publishingHint: config.publishingHint,
				recommendedNames: config.recommendedNames,
			} satisfies PresentationEntry;
		}),
	);

	return entries.sort((left, right) => {
		if (left.order !== right.order) {
			return left.order - right.order;
		}

		if (left.featured !== right.featured) {
			return left.featured ? -1 : 1;
		}

		return naturalCompare(left.title, right.title);
	});
}

const collectionsPromise: Promise<PresentationCollectionSummary[]> = (async () => {
	const keys = Object.keys(collectionConfigs) as PresentationCollection[];
	const entriesByCollection = await Promise.all(
		keys.map(async (key) => ({
			key,
			entries: await getCollectionEntries(key),
		})),
	);

	return entriesByCollection.map(({ key, entries }) => ({
		key,
		label: collectionConfigs[key].label,
		description: collectionConfigs[key].description,
		path: `/presentations/${key}`,
		publishingHint: collectionConfigs[key].publishingHint,
		recommendedNames: collectionConfigs[key].recommendedNames,
		entries,
		entryCount: entries.length,
		assetReadyCount: entries.filter((entry) => entry.hasAssets).length,
	}));
})();

export async function getPresentationCollections() {
	return collectionsPromise;
}

export async function getPresentationEntries() {
	const collections = await getPresentationCollections();
	return collections.flatMap((collection) => collection.entries);
}

export async function getPresentationCollection(collection: string) {
	const collections = await getPresentationCollections();
	return collections.find((entry) => entry.key === collection);
}

export async function getPresentationEntry(collection: string, slug: string) {
	const entries = await getPresentationEntries();
	return entries.find((entry) => entry.collection === collection && entry.slug === slug);
}
