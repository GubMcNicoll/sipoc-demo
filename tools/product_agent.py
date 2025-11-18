#!/usr/bin/env python3
"""Product classification agent

Reads a WI CSV and classifies each WKI_Summary into product area / product candidate and feature description
using rules from SourceDocuments/classifyingproducts.md and alias mappings in SourceDocuments/productalias.md.

Outputs a CSV with additional columns: product_area_raw,product_area_canonical,product_candidate,feature_description
"""
import csv
import argparse
import re
from pathlib import Path


def load_aliases(path: Path):
    """Parse productalias.md and return a mapping alias -> canonical"""
    aliases = {}
    text = path.read_text(encoding="utf-8")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('```'):
            continue
        # pattern: alias1, alias2 = Canonical Name
        if '=' in line:
            left, right = line.split('=', 1)
            canonical = right.strip()
            left = left.strip()
            # aliases may be comma separated
            for a in left.split(','):
                a = a.strip()
                # remove trailing colons or parentheses markers like AM:
                a = a.rstrip(':')
                if a:
                    aliases[a.upper()] = canonical
    return aliases


def normalise_area(raw: str):
    if raw is None:
        return ''
    s = raw.strip()
    # strip surrounding brackets
    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1].strip()
    return s


def classify_summary(summary: str, aliases: dict):
    """Apply rules from classifyingproducts.md to extract product area, candidate and feature desc."""
    s = (summary or '').strip()
    product_area_raw = ''
    product_area_canonical = ''
    product_candidate = ''
    feature_description = ''

    # Rule 1: if colon present, text before colon = product area/code
    if ':' in s:
        before, after = s.split(':', 1)
        product_area_raw = normalise_area(before)
        title = after.strip()
        # If hyphen in title, split
        if '-' in title:
            cand, desc = title.split('-', 1)
            product_candidate = cand.strip()
            feature_description = desc.strip()
        else:
            product_candidate = title
            feature_description = ''
    else:
        # No colon
        if '-' in s:
            cand, desc = s.split('-', 1)
            product_candidate = cand.strip()
            feature_description = desc.strip()
        else:
            # neither colon nor hyphen: whole summary as product candidate
            product_candidate = s
            feature_description = ''

    # Normalise product_area via aliases if available
    if product_area_raw:
        key = product_area_raw.upper()
        product_area_canonical = aliases.get(key, '')
        if not product_area_canonical:
            # fallback: if the raw looks like a code (short), keep as-is
            product_area_canonical = product_area_raw
    else:
        product_area_canonical = ''

    # Further normalisation: if candidate contains known product area prefix (e.g. 'EG e-Invoice')
    # keep candidate trimmed
    product_candidate = product_candidate.strip()
    feature_description = feature_description.strip()

    return {
        'product_area_raw': product_area_raw,
        'product_area_canonical': product_area_canonical,
        'product_candidate': product_candidate,
        'feature_description': feature_description,
    }


def process(input_csv: Path, alias_md: Path, output_csv: Path):
    aliases = load_aliases(alias_md)
    with input_csv.open(newline='', encoding='utf-8') as inf, output_csv.open('w', newline='', encoding='utf-8') as outf:
        reader = csv.DictReader(inf)
        fieldnames = reader.fieldnames[:] if reader.fieldnames else []
        extras = ['product_area_raw', 'product_area_canonical', 'product_candidate', 'feature_description']
        for e in extras:
            if e not in fieldnames:
                fieldnames.append(e)
        writer = csv.DictWriter(outf, fieldnames=fieldnames)
        writer.writeheader()
        counts = {}
        # collect structure for markdown output: area -> product -> set(features)
        md_tree = {}
        for row in reader:
            summary = row.get('WKI_Summary', '')
            classification = classify_summary(summary, aliases)
            row.update(classification)
            writer.writerow(row)
            area = classification.get('product_area_canonical') or '(none)'
            counts[area] = counts.get(area, 0) + 1
            # collect into md_tree
            prod = classification.get('product_candidate') or '(unknown)'
            feat = classification.get('feature_description') or ''
            md_tree.setdefault(area, {})
            md_tree[area].setdefault(prod, set())
            if feat:
                md_tree[area][prod].add(feat)

    print(f'Wrote classified output to: {output_csv}')
    print('Counts by product area:')
    for k, v in sorted(counts.items(), key=lambda x: -x[1]):
        print(f'  {k}: {v}')
    return md_tree


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', '-i', default='SourceDocuments/WIData-lastyr.csv')
    p.add_argument('--aliases', '-a', default='SourceDocuments/productalias.md')
    p.add_argument('--output', '-o', default='tools/output_classified.csv')
    p.add_argument('--md', dest='md', default='tools/features_products.md',
                   help='Write markdown list of products/features to this path')
    args = p.parse_args()
    md_tree = process(Path(args.input), Path(args.aliases), Path(args.output))
    # write markdown
    md_path = Path(args.md)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    with md_path.open('w', encoding='utf-8') as md:
        md.write('# Products and Features\n\n')
        for area in sorted(md_tree.keys()):
            md.write(f'## Product Area: {area}\n\n')
            products = md_tree[area]
            for prod in sorted(products.keys()):
                md.write(f'### Product: {prod}\n\n')
                feats = products[prod]
                if feats:
                    for f in sorted(feats):
                        md.write(f'- {f}\n')
                else:
                    md.write('- (no feature description)\n')
                md.write('\n')

    print(f'Wrote markdown features/products to: {md_path}')


if __name__ == '__main__':
    main()
