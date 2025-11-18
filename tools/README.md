# Product agent (tools)

This folder contains a small Python agent to classify work item summaries (`WKI_Summary`) using the repository's product classification rules.

Files
- `product_agent.py` — reads `SourceDocuments/WIData-lastyr.csv` and `SourceDocuments/productalias.md`, applies the rules from `classifyingproducts.md`, and writes `tools/output_classified.csv`.

Quick run (PowerShell on Windows)

Run with the bundled defaults (reads `SourceDocuments/WIData-lastyr.csv` and writes `tools/output_classified.csv`):

```powershell
python .\tools\product_agent.py
```

Or specify paths explicitly:

```powershell
python .\tools\product_agent.py -i .\SourceDocuments\WIData-lastyr.csv -a .\SourceDocuments\productalias.md -o .\tools\output_classified.csv
```

Notes
- The script implements a minimal interpretation of the rules in `classifyingproducts.md`:
  - If a colon (:) exists in the summary, the text before the colon is treated as the product area/code; the text after is the working title.
  - If a hyphen (-) exists in the working title (or the whole summary when no colon), the text before the first hyphen is treated as the product candidate and after as the feature description.
  - Product area aliases are read from `productalias.md` and applied (case-insensitive).

This is intentionally small and local — it's safe to run and inspect the output. If you'd like the agent to apply more advanced dictionary lookups (embedded product words, fuzzy matching, or rules for stripping project codes like `AM:`), I can extend it.
