1. Indicators of major features
These usually reflect substantial new capability, regulatory compliance shifts, new markets, or structural enhancements.
A. Regulatory enablement or new-country entry
Look for wording like:
“Colombia – New…”
“Dominican Republic – Set…”
“Montenegro – Add…”
“Costa Rica – New…”
“TR e-Invoice – …”
“EU ICS2 – R3…”
“NCTS P5…”
This is almost always major, because it unlocks market access or regulatory compliance in a jurisdiction.
B. First-time support for major industry frameworks
Examples:
“IATA DGR 66th edition update”
“Dangerous Goods: IMDG Code update”
“ICS2 R3”
“SAF-T NO v3”
“CARM”
These represent whole-of-system shifts.
C. Major module-level new functionality
Signals:
“New feature”, “new module”, “new macro”, “add ability to…”
“Feature flag removal” (often meaning feature is now GA)
“Convert multiple consignments into one job”
“Bulk delivery feature”
D. Structural system enhancements / performance-critical redesign
Terms like:
“Rework”
“Refactor”
“Schema change”
“Core behaviour update”
“Major UX Improvements” (not tweaks)
“New API”, “API v3 support”
“Index Search support for module” (when enabling large modules)
E. Foundational commodity/compliance capability
Anything under CPW (ComplianceWise), CO2, CARM, ICS2, NCTS5 that adds:
new behaviours
new risk categories
new data structures
new automation
2. Indicators of minor fixes
These are mostly patch-level adjustments.
A. Obvious textual cues
“fix”
“minor fix”
“correction”
“typo”
“caption”
“rename”
“update wording”
“validation change”
“mapping change”
“defaulting rule”
“remove audit event”
“hide tab”
“expose field”
“add column”
“add warning”
B. Small enhancements within an existing workflow
Examples:
“Add inspection type”
“Add a filter to grid”
“Expose a field”
“Enhance error message”
“Improve label printing speed”
“Prevent posting negative value”
“Copy previous invoice line”
These don’t change core behaviour; they polish it.
3. Mid-tier signals (requires judgement)
Some phrases don't automatically mean “big” or “small.”
Might be major or minor:
“Enhancement”
“Support for…”
“Allow…”
“New report”
“Update note”
“Integration improvements”
“Add registry setting”
“Add logic”
Here context matters:
If it touches compliance or country enablement → often major
If it touches UI, logging, defaults → minor
4. A usable rule set for automated classification
Here’s a classification approach you could run on your data (even in Excel, Power BI, or Python).
This is tuned to your domain (CargoWise, global customs, logistics modules).
Major feature rules (if ANY are true → major)
Summary includes a country name plus new tax, compliance, or e-Invoice requirement
(Regex-ish: contains a country code or name AND “New”, “Add”, “Enable”, “Support”, “Compliance”, “Tax”, “E-invoice”)
Mentions updating to or supporting a major regulatory framework
Mentions new module, new macro, new feature, new form, new API, new schema, new data model
Contains “R2”, “R3”, “Phase 2”, “TP5”, “P5” (versioned multi-phase compliance work)
Mentions CARM, ICS2, NCTS, ComplianceWise, CO2, Dangerous Goods, IATA DGR, IMDG, Peppol, SAF-T, CARM, e-Invoicing and is NOT clearly a wording change
Mentions enabling new-country support
Mentions converting or consolidating base business objects
(“Convert multiple consignments”, “Bulk convert parties to orgs”, etc.)
Minor fix rules (if NONE of the above AND ANY of the below → minor)
Contains: fix, minor, update wording, mapping, defaulting, rename
“Expose field”, “Add column”, “Add filter”, “Add warning”, “Hide tab”, “Remove audit event”
Validation-only changes
Adjustments to error messages or logs
Performance tweaks (unless module-level, which could be major)
Caption changes
Grid changes
Default value changes
Cosmetic or process safety hints
“Ability to…” when limited to UI (not business logic)
Fallback heuristic
If it:
affects tax, regulatory compliance, new functionality, or an integration
→ treat as major.
If it:
affects UI, clarity, report formatting, or a single field
→ treat as minor.
