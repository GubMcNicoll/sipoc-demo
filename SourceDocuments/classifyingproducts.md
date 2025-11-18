For each WKI_Summary:

If there is a colon :

Text before the colon is a product area / code

e.g.

CPW: ComplianceWise enabled by default and support only
→ Product area = CPW (later map CPW → ComplianceWise)

PP: Stock on Hand Report By Location and Stock Movement Report
→ Product area = PP

Text after the colon is your working title for the feature; then:

If there is a hyphen -, take text before the first hyphen as feature “short name” and after the first hyphen as feature “description”.

EG e-Invoice - Add Bank Account Details to AR e-Invoice Submission XML
→ Product candidate = EG e-Invoice
→ Feature = Add Bank Account Details to AR e-Invoice Submission XML

If there is no colon but there is a hyphen -

Text before first hyphen = product candidate

Text after first hyphen = feature description

e.g.

Total Allocation Statistics Section UI Enhancements
→ Product candidate = Total Allocation Statistics Section (but see 3.2)
→ Feature = UI Enhancements

[CCA] Consol ETD should NOT check Allocation Route Period if Booking/MBL exist
→ Product area = [CCA] (strip brackets)
→ Feature = Consol ETD should NOT check Allocation Route Period if Booking/MBL exist

If there is neither

Treat full WKI_Summary as a feature name and look for embedded product words via dictionaries (next sections).

3.2 Normalise the primary product

Once you have the “product candidate” from 3.1, clean it with:

Strip known prefixes / wrappers:

Leading and trailing brackets: [CCA], [LIC], [S2S] → keep CCA, LIC, S2S as product areas.

Common project codes like AM:, DMN:, S&S GB, EU ICS2, CCSUK, Dangerous Goods: etc should be mapped to canonical product names via a lookup table.
