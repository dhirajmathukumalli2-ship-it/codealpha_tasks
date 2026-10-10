# Language Translation Tool

A responsive browser translation utility for entering text, choosing a language pair, translating through MyMemory, and copying the result.

## Run & Operate

- `pnpm --filter @workspace/language-translation-tool run dev` — run the translation tool through the managed preview workflow
- `pnpm --filter @workspace/language-translation-tool run typecheck` — typecheck the Vite package
- `pnpm run typecheck` — run the full workspace typecheck
- `pnpm --filter @workspace/language-translation-tool run build` — build the static frontend bundle

The browser calls the public MyMemory Translation API directly. No API key or database is required.

## Stack

- pnpm workspaces, Node.js 24, TypeScript 5.9
- API: Express 5
- DB: PostgreSQL + Drizzle ORM
- Validation: Zod (`zod/v4`), `drizzle-zod`
- API codegen: Orval (from OpenAPI spec)
- Build: esbuild (CJS bundle)

## Where things live

- `artifacts/language-translation-tool/index.html` — page entry point and metadata
- `artifacts/language-translation-tool/style.css` — responsive visual styling
- `artifacts/language-translation-tool/script.js` — language options, API request, loading/error states, and copy behavior
- `artifacts/language-translation-tool/.replit-artifact/artifact.toml` — artifact preview and workflow configuration

## Architecture decisions

- The frontend is intentionally vanilla HTML, CSS, and JavaScript so the internship task can be inspected without a framework-specific abstraction layer.
- MyMemory is used as a public translation endpoint, keeping setup keyless for a browser-only demo.
- Translation failures are rendered in the output area instead of silently falling back to the source phrase.
- The output is escaped before it is inserted into the DOM, and copy uses the Clipboard API with a browser fallback.

## Product

- Choose from 13 common source and target languages.
- Swap the language pair.
- Translate up to 500 characters.
- See loading, empty-input, success, and API-failure states.
- Copy a completed translation to the clipboard.

## User preferences

- The user requested a functional project organized around `index.html`, `style.css`, and `script.js`.

## Gotchas

- The tool depends on the MyMemory public API being reachable from the browser.
- The web artifact must be run through its managed workflow so `PORT` and `BASE_PATH` are provided.

## Pointers

- See the `pnpm-workspace` skill for workspace structure, TypeScript setup, and package details
