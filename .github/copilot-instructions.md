# Copilot / AI agent instructions for this repository

This project is a small, static SIPOC diagram editor. The goal of an AI coding agent working here is to make safe, minimal edits to the embedded JSON data in the HTML and to document or improve the editing experience. Keep changes non-invasive unless the user asks for a refactor.

Key places to look
- `SIPOC/sipoc-diagram.html` — the main artifact. It contains the interactive diagram and a `<script id="embedded-data">` block with the JSON model.
- `README.md` — canonical explanation of the JSON shape, ID conventions, connection rules, color CSS classes, and manual test steps.
- `SourceDocuments/` — supporting docs and CSVs (not part of runtime). Use these only for reference when creating example data.

Big-picture architecture and data flow (short)
- Single static HTML app: JSON (embedded) → DOM rendering → SVG connections. There is no backend, build pipeline, or bundler in this repo.
- Editing flow: update the JSON in the `<script id="embedded-data">` block, save the HTML, refresh the browser, then click nodes to verify the side panel and connection highlights.

Project conventions you must follow
- ID format: `category-number` (e.g. `supplier-1`, `input-5`). IDs are case-sensitive and must be unique across all node arrays.
- Node fields: use the fields shown in `README.md` (e.g. `id`, `name`, `description`, plus category-specific fields like `requirements`, `specifications`, `activities`, `deliverables`, `segment`). Match existing keys — don't invent new fields unless adding optional UX features and documenting them.
- Connections: objects of shape `{ "from": "id", "to": "id" }`. Only connect adjacent SIPOC levels (Suppliers→Inputs→Process→Outputs→Customers) unless the user explicitly requests a different visualization.

Examples (copy when making edits)
- Add a node: copy an existing node object in the correct array, bump the number in the `id` and fill `name`/`description`.
- Add a connection: append `{ "from": "supplier-3", "to": "input-9" }` to the `connections` array.

Styling/CSS facts to reference
- Category CSS classes live in the `<style>` section of `SIPOC/sipoc-diagram.html`:
  - `.node.suppliers`, `.node.inputs`, `.node.process`, `.node.outputs`, `.node.customers`
  - Label classes: `.label.suppliers`, etc.
  - Connection lines: `.connection-line` and `.connection-line.active`

Developer workflows (explicit)
- No build: open `SIPOC/sipoc-diagram.html` in a browser (file://) and refresh after edits.
- Manual verification steps: save HTML → refresh → click nodes → verify side panel and connection highlighting (see `README.md` Testing section).

When to alter code vs. docs
- Prefer editing the embedded JSON or README examples for content changes.
- If you change the HTML structure or CSS, include a short comment in the HTML and update `README.md` with the new locations/keys.

Integration / external dependencies
- None in-repo. If the user asks to integrate with an external service (APIs, model toggles, feature flags), ask for credentials and an explicit acceptance of storing secrets; otherwise provide documentation-only changes.

About "Enable Claude Sonnet 4.5 for all clients"
- This appears to be an operational request outside the repository (enabling an AI model for clients). Document-level guidance only: if you want this action to be tracked in the repo, clarify whether you want:
  1) a README/CONTRIBUTING note describing how to turn on Claude Sonnet 4.5 in your hosting/service dashboard, or
  2) an infra/CI change (requires credentials and access to the external service), or
  3) a repository-level feature flag or policy document.
- Do not attempt to perform external enablement from the repo without explicit credentials and instructions.

If you modify or add data files
- Keep examples minimal and well-formed JSON. Run a JSON syntax check locally before committing.

Safety and minimalism
- Avoid large refactors. This repo is a single-file interactive diagram; the safest useful changes are clearer docs, better example JSON, small CSS tweaks, or small UX fixes (label text, spacing). When in doubt, add documentation and tests/examples instead of invasive changes.

Questions or unclear cases
- If a requested change touches multiple responsibilities (data shape → rendering → styling), stop and ask for confirmation, and list the affected files: typically `SIPOC/sipoc-diagram.html` and `README.md`.

Signed-off-by: repo guidance
