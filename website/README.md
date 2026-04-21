# Persistence Theory Website

Public-facing Astro site for the Persistence Theory project. This app is the presentation layer for the research workspace in `../Formalization`, not the source-of-truth for the formal proofs themselves.

## Current scope

- Landing page for the project and its visual identity
- Theory page for the ACP / CDT conceptual map
- Program page for active fronts, open problems, and workspace structure

## Project structure

```text
website/
├── public/
│   └── favicon.svg
├── src/
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       ├── index.astro
│       ├── program.astro
│       └── theory.astro
└── package.json
```

## Commands

Run commands from `website/`.

| Command | Action |
| :------ | :----- |
| `npm install` | Install dependencies |
| `npm run dev` | Start local dev server |
| `npm run build` | Build static site into `dist/` |
| `npm run preview` | Preview the production build locally |

## Deploy to Vercel

If this workspace becomes a repo with both `Formalization/` and `website/`, set the Vercel project root directory to `website`.

- Framework preset: Astro
- Install command: `npm install`
- Build command: `ASTRO_TELEMETRY_DISABLED=1 npm run build`
- Output directory: `dist`

### Typical flow

1. Push the workspace to GitHub, GitLab, or Bitbucket.
2. Import the repo into Vercel.
3. Set the root directory to `website`.
4. Confirm the build/output settings above.
5. Deploy.

### CLI option

If you prefer the CLI later, run Vercel commands from `website/` so the deployment target is the site app rather than the research workspace.

## Notes

- Astro telemetry may try to write outside the workspace in some sandboxed environments. If that happens locally, run commands with `ASTRO_TELEMETRY_DISABLED=1`.
- The next natural step is importing selected material from `../Formalization` into native website content pages or MDX collections.
