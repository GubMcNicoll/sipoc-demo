#!/usr/bin/env python3
"""
analyze_widata.py

Reads instructions/majorfeature.md to build a simple rule set and
applies it to SourceDocuments/WIData-lastyr.csv. Writes a Markdown
report to output/analysis-from-majorfeature.md summarising the
predicted classification (major/minor/uncertain), matched keywords,
and mismatches vs any existing `Classification` column in the CSV.

Usage: python tools/analyze_widata.py
"""
import re
import csv
import os
from collections import Counter, defaultdict


def read_file(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def build_patterns(md_text):
    # Heuristic extraction: find some explicit rule sections if present
    major_block = ''
    minor_block = ''
    lo = md_text.lower()
    mi = lo.find('major feature rules')
    mj = lo.find('minor fix rules')
    if mi != -1:
        if mj != -1 and mj > mi:
            major_block = md_text[mi:mj]
            # try to find the following minor block
            rest = md_text[mj:]
            # minor block end is next blank line double newline or end
            minor_block = rest
        else:
            major_block = md_text[mi:]
    elif 'major feature rules (if any are true' in lo:
        # fallback
        s = lo.find('major feature rules')
        major_block = md_text[s:]

    # Collect candidate phrases from the md and also add a curated list
    def extract_phrases(block):
        phrases = set()
        for line in block.splitlines():
            line = line.strip().strip('-•')
            if not line:
                continue
            # split by commas, ' or ' and ' / '
            parts = re.split(r"[,/]| and | or |\(|\)", line)
            for p in parts:
                p = p.strip().strip('"')
                if len(p) >= 3 and len(p) < 120:
                    # ignore very generic words
                    if p.lower() in ('this', 'these', 'here', 'that'):
                        continue
                    phrases.add(p)
        return phrases

    major_phrases = extract_phrases(major_block)
    minor_phrases = extract_phrases(minor_block)

    # Add curated tokens from the instructions to be conservative
    curated_major = [
        r'new', r'add', r'enable', r'support', r'compliance', r'tax', r'e-?invoice',
        r'regulatory', r'new module', r'new feature', r'new form', r'new api', r'schema',
        r'data model', r'convert', r'bulk', r'R2', r'R3', r'P5', r'TP5', r'Phase 2',
        r'CARM', r'ICS2', r'NCTS', r'ComplianceWise', r'CO2', r'Dangerous Goods',
        r'IATA DGR', r'IMDG', r'Peppol', r'SAF-T'
    ]

    curated_minor = [
        r'fix', r'minor', r'correction', r'typo', r'caption', r'rename', r'update wording',
        r'mapping', r'default', r'validation', r'expose field', r'add column', r'add filter',
        r'add warning', r'hide tab', r'remove audit', r'performance', r'improve', r'enhance'
    ]

    # Build regex patterns (case-insensitive)
    major_patterns = [re.compile(r"\b" + re.escape(p) + r"\b", re.I) for p in major_phrases if len(p) > 0]
    minor_patterns = [re.compile(r"\b" + re.escape(p) + r"\b", re.I) for p in minor_phrases if len(p) > 0]
    # add curated
    major_patterns += [re.compile(p, re.I) for p in curated_major]
    minor_patterns += [re.compile(p, re.I) for p in curated_minor]

    return major_patterns, minor_patterns


def parse_product_aliases(md_text):
    """Parse productalias.md into a map of alias -> canonical name."""
    alias_map = {}
    for line in md_text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        # Expect format like: "CPW, ComplianceWise = ComplianceWise"
        if '=' in line:
            left, right = line.split('=', 1)
            canonical = right.strip()
            # aliases split by comma
            aliases = [a.strip() for a in left.split(',') if a.strip()]
            for a in aliases:
                alias_map[a.lower()] = canonical
    return alias_map


def detect_product(summary, alias_map):
    """Detect product candidate from summary and map to canonical product where possible.

    Returns (product_candidate, canonical_product, matched_aliases)
    """
    if not summary:
        return None, None, []

    s = summary.strip()
    product_candidate = None

    # If there's a colon, text before colon is product area
    if ':' in s:
        candidate = s.split(':', 1)[0].strip()
        product_candidate = candidate
    else:
        # check for leading bracketed code like [CCA]
        m = re.match(r"^\s*\[([^\]]+)\]\s*(.*)$", s)
        if m:
            product_candidate = m.group(1).strip()
        elif '-' in s:
            product_candidate = s.split('-', 1)[0].strip()
        else:
            # fallback: take up to first 6-7 words as candidate
            words = s.split()
            product_candidate = ' '.join(words[:6]).strip()

    if product_candidate:
        pc = product_candidate.strip().strip('[]')
    else:
        pc = None

    matched_aliases = []
    canonical = None
    if pc:
        low = pc.lower()
        # direct alias match
        if low in alias_map:
            canonical = alias_map[low]
            matched_aliases.append(pc)
        else:
            # try substring match both ways
            for alias, canon in alias_map.items():
                if alias in low or low in alias:
                    canonical = canon
                    matched_aliases.append(alias)
                    break
    # Also scan full summary for alias mentions
    if not canonical:
        for alias, canon in alias_map.items():
            if re.search(r"\b" + re.escape(alias) + r"\b", s, re.I):
                canonical = canon
                matched_aliases.append(alias)
                break

    return pc, canonical, matched_aliases


def classify_text(text, major_patterns, minor_patterns):
    matches = {'major': [], 'minor': []}
    for p in major_patterns:
        if p.search(text):
            matches['major'].append(p.pattern)
    for p in minor_patterns:
        if p.search(text):
            matches['minor'].append(p.pattern)

    if matches['major']:
        return 'major', matches
    if matches['minor']:
        return 'minor', matches
    return 'uncertain', matches


def main():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    md_path = os.path.join(root, 'instructions', 'majorfeature.md')
    classprod_path = os.path.join(root, 'instructions', 'classifyingproducts.md')
    alias_path = os.path.join(root, 'instructions', 'productalias.md')
    csv_path = os.path.join(root, 'SourceDocuments', 'WIData-lastyr.csv')
    out_dir = os.path.join(root, 'output')
    os.makedirs(out_dir, exist_ok=True)
    out_md = os.path.join(out_dir, 'analysis-from-majorfeature.md')
    out_products_csv = os.path.join(out_dir, 'product_assignments.csv')

    md_text = read_file(md_path)
    major_patterns, minor_patterns = build_patterns(md_text)
    # read product alias and classifying rules
    alias_map = {}
    try:
        alias_md = read_file(alias_path)
        alias_map = parse_product_aliases(alias_md)
    except Exception:
        alias_map = {}

    # optional: classifying products rules (not heavily used, kept for future)
    try:
        classprod_md = read_file(classprod_path)
    except Exception:
        classprod_md = ''

    rows = []
    with open(csv_path, newline='', encoding='utf-8', errors='replace') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            rows.append(r)

    summary_counter = Counter()
    keyword_counter = Counter()
    mismatches = []

    analyses = []
    for r in rows:
        # Combine useful text fields
        text_fields = []
        for k in ('WKI_Summary', 'details', 'P9_Description', 'WKI_Status', 'Explanation'):
            if k in r and r[k]:
                text_fields.append(r[k])
        text = '\n'.join(text_fields)
        predicted, matches = classify_text(text, major_patterns, minor_patterns)
        # detect product candidate and map to canonical product where possible
        product_candidate, product_canonical, matched_aliases = detect_product(r.get('WKI_Summary',''), alias_map)
        analyses.append((r, predicted, matches, product_candidate, product_canonical, matched_aliases))
        summary_counter[predicted] += 1
        for t in matches['major'] + matches['minor']:
            keyword_counter[t] += 1

        existing = r.get('Classification', '').strip().lower()
        if existing and existing not in ('major', 'minor'):
            # allow values like empty or other labels
            existing = existing
        if existing and existing != predicted:
            mismatches.append((r.get('WKI_WorkItemNumber') or r.get('WKI_WorkItemNumber', ''), r.get('WKI_Summary',''), existing, predicted, matches))

    # write product assignments CSV
    try:
        import csv as _csv
        with open(out_products_csv, 'w', newline='', encoding='utf-8') as pcsv:
            fieldnames = ['WKI_WorkItemNumber','WKI_Summary','CSV_Classification','Predicted','ProductCandidate','ProductCanonical','MatchedAliases']
            writer = _csv.DictWriter(pcsv, fieldnames=fieldnames)
            writer.writeheader()
            for (r, predicted, matches, product_candidate, product_canonical, matched_aliases) in analyses:
                writer.writerow({
                    'WKI_WorkItemNumber': r.get('WKI_WorkItemNumber',''),
                    'WKI_Summary': r.get('WKI_Summary',''),
                    'CSV_Classification': r.get('Classification',''),
                    'Predicted': predicted,
                    'ProductCandidate': product_candidate or '',
                    'ProductCanonical': product_canonical or '',
                    'MatchedAliases': ';'.join(matched_aliases) if matched_aliases else ''
                })
    except Exception:
        pass

    # Write Markdown report
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write('# Analysis from majorfeature rules\n\n')
        f.write('This report classifies work items as major/minor/uncertain using heuristics derived from `instructions/majorfeature.md`.\n\n')

        f.write('## Summary\n\n')
        total = sum(summary_counter.values())
        f.write(f'- Total rows analysed: {total}\n')
        for k in ('major', 'minor', 'uncertain'):
            f.write(f'- Predicted {k}: {summary_counter.get(k,0)}\n')
        f.write('\n')

        f.write('## Keyword matches (top 30)\n\n')
        for word, cnt in keyword_counter.most_common(30):
            f.write(f'- `{word}` : {cnt}\n')
        f.write('\n')

        # Product summary
        f.write('## Product assignments summary\n\n')
        prod_counts = Counter()
        for (_r, _pred, _matches, pc, canonical, _ma) in analyses:
            prod_counts[canonical or (pc or 'Unknown')] += 1
        for prod, cnt in prod_counts.most_common():
            f.write(f'- {prod}: {cnt}\n')
        f.write('\n')

        f.write('## Mismatches vs CSV Classification\n\n')
        f.write(f'- Total mismatches: {len(mismatches)}\n\n')
        if mismatches:
            f.write('| WorkItem | Summary | CSV Classification | Predicted | Matched patterns |\n')
            f.write('|---|---|---:|---|---|\n')
            for wi, summary, existing, predicted, matches in mismatches:
                matched = ', '.join((matches['major'][:3] if matches['major'] else matches['minor'][:3]))
                # truncate summary
                s = (summary[:80] + '...') if len(summary) > 80 else summary
                f.write(f'| {wi} | {s} | {existing} | {predicted} | {matched} |\n')
        else:
            f.write('No mismatches found.\n')

        f.write('\n')
        f.write('## Examples (first 20 rows)\n\n')
        f.write('| WorkItem | Summary | Predicted | Product | Matched patterns | Explanation snippet |\n')
        f.write('|---|---|---:|---|---|---|\n')
        for (r, predicted, matches, product_candidate, product_canonical, matched_aliases) in analyses[:20]:
            wi = r.get('WKI_WorkItemNumber','')
            summary = r.get('WKI_Summary','').replace('\n',' ')[:80]
            prod = product_canonical or (product_candidate or '')
            matched = ', '.join((matches['major'][:3] if matches['major'] else matches['minor'][:3]))
            expl = (r.get('Explanation') or r.get('details') or '')[:100].replace('\n',' ')
            f.write(f'| {wi} | {summary} | {predicted} | {prod} | {matched} | {expl} |\n')

    print('Wrote report to', out_md)


if __name__ == '__main__':
    main()
