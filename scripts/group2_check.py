#!/usr/bin/env python3
"""One-off: cross-reference Group 2 phantoms (no DB SNF match) against CMS source."""

import csv
from utils import load_cms_snf, safe


def main():
    _, cms_rows = load_cms_snf()
    cms_by_ccn = {}
    for row in cms_rows:
        ccn = safe(row.get('CMS Certification Number (CCN)'))
        if ccn:
            ccn_clean = ccn.split('.')[0]
            cms_by_ccn[ccn_clean] = row

    print(f'CMS CCN index: {len(cms_by_ccn)} entries')

    phantoms = []
    with open('audit_reports/nic_enrichment.csv', 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if (row['classification'] == 'PHANTOM'
                    and row['do_we_serve'] != 'Yes'
                    and 'ADDR_MATCHES_DB_SNF' not in row['tags']):
                phantoms.append(row)

    with_ccn = [p for p in phantoms if p['nic_ccn']]
    without_ccn = [p for p in phantoms if not p['nic_ccn']]

    print(f'Group 2: {len(phantoms)} total, {len(with_ccn)} with CCN, {len(without_ccn)} without')
    print()

    print('=== 7 WITH NIC CCN — Do they exist in our CMS source? ===')
    print()
    for p in with_ccn:
        ccn = p['nic_ccn'].split('.')[0]
        cms = cms_by_ccn.get(ccn)
        print(f'Row {p["excel_row"]}: {p["facility"]}')
        print(f'  DB:  {p["address"]}, {p["city"]}, {p["state"]}')
        print(f'  NIC: NC={p["nc_units"]} IL={p["il_units"]} | CCN={ccn}')
        if cms:
            print(f'  CMS: FOUND — {safe(cms.get("Provider Name"))}')
            print(f'       {safe(cms.get("Provider Address"))}, {safe(cms.get("City/Town"))} {safe(cms.get("State"))}')
            print(f'       Beds={safe(cms.get("Number of Certified Beds"))} Census={safe(cms.get("Average Number of Residents per Day"))}')
            print(f'       Chain: {safe(cms.get("Chain Name")) or "(none)"}')
        else:
            print(f'  CMS: *** NOT IN OUR CMS SOURCE FILE ***')
        print()

    print('=== 4 WITHOUT CCN ===')
    print()
    for p in without_ccn:
        print(f'Row {p["excel_row"]}: {p["facility"]}')
        print(f'  {p["address"]}, {p["city"]}, {p["state"]}')
        print(f'  NC={p["nc_units"]} IL={p["il_units"]}')
        print(f'  Corp: {p["corporate_name"] or "(blank)"}')
        print()


if __name__ == '__main__':
    main()
