import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # archive: find utils.py
#!/usr/bin/env python3
"""One-off: detailed side-by-side of served confirmed phantoms + their SNF pairs."""

import csv
from utils import load_db, addr_key, safe


def main():
    _, db_rows = load_db()

    # SNF lookup by address key
    snf_by_key = {}
    for row in db_rows:
        if safe(row.get('Source_Type')) == 'SNF':
            key = addr_key(safe(row.get('Address')), safe(row.get('City')), safe(row.get('State')))
            if key and key != '||':
                snf_by_key[key] = row

    # ALF lookup by excel_row
    alf_by_row = {}
    for row in db_rows:
        if safe(row.get('Source_Type')) == 'ALF':
            alf_by_row[row['_excel_row']] = row

    # Read enrichment CSV
    phantoms = []
    with open('audit_reports/nic_enrichment.csv', 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row['classification'] == 'PHANTOM' and row['do_we_serve'] == 'Yes':
                phantoms.append(row)

    phantoms.sort(key=lambda r: (r['state'], r['city']))

    print(f'SERVED CONFIRMED PHANTOMS: {len(phantoms)} ALF rows')
    print(f'Each paired with the SNF row at the same address')
    print()

    for i, p in enumerate(phantoms, 1):
        excel_row = int(p['excel_row'])
        alf = alf_by_row.get(excel_row, {})
        key = addr_key(safe(alf.get('Address')), safe(alf.get('City')), safe(alf.get('State')))
        snf = snf_by_key.get(key, {})

        print('=' * 80)
        print(f'PAIR #{i}: {p["city"]}, {p["state"]}')
        print('=' * 80)
        print()
        print(f'  ALF ROW {excel_row} (would be REMOVED)')
        print(f'    Facility:      {safe(alf.get("Facility_Name"))}')
        print(f'    Corporate:     {safe(alf.get("Corporate_Name")) or "(blank)"}')
        print(f'    Ownership:     {safe(alf.get("Ownership_Type"))}')
        print(f'    Beds:          {safe(alf.get("Total_Beds"))}')
        print(f'    Census:        {safe(alf.get("Census"))}')
        print(f'    Do_We_Serve:   {safe(alf.get("Do_We_Serve"))}')
        print(f'    Integrated:    {safe(alf.get("Integrated_Flag"))}')
        print(f'    PCP_Flag:      {safe(alf.get("PCP_Flag"))}')
        print(f'    MH_Flag:       {safe(alf.get("MH_Flag"))}')
        print(f'    Barrier:       {safe(alf.get("Barrier")) or "(none)"}')
        print(f'    Contract:      {safe(alf.get("Contract_Status"))}')
        print(f'    Geo Tier:      {safe(alf.get("Geographic_Tier"))}')
        print(f'    Metro:         {safe(alf.get("Metro_Assignment")) or "(none)"}')
        print(f'    Address:       {safe(alf.get("Address"))}')
        print(f'    NIC Operator:  {p["nic_operator"]}')
        print(f'    NIC Owner:     {p["nic_owner"]}')
        print(f'    NIC CCN:       {p["nic_ccn"] or "(none)"}')
        print(f'    NIC Units:     NC={p["nc_units"]} AL={p["al_units"]} MC={p["mc_units"]} IL={p["il_units"]} AA={p["aa_units"]}')
        print()

        if snf:
            snf_row = snf['_excel_row']
            print(f'  SNF ROW {snf_row} (STAYS)')
            print(f'    Facility:      {safe(snf.get("Facility_Name"))}')
            print(f'    Corporate:     {safe(snf.get("Corporate_Name")) or "(blank)"}')
            print(f'    Ownership:     {safe(snf.get("Ownership_Type"))}')
            print(f'    Beds:          {safe(snf.get("Total_Beds"))}')
            print(f'    Census:        {safe(snf.get("Census"))}')
            print(f'    Do_We_Serve:   {safe(snf.get("Do_We_Serve"))}')
            print(f'    Integrated:    {safe(snf.get("Integrated_Flag"))}')
            print(f'    PCP_Flag:      {safe(snf.get("PCP_Flag"))}')
            print(f'    MH_Flag:       {safe(snf.get("MH_Flag"))}')
            print(f'    Barrier:       {safe(snf.get("Barrier")) or "(none)"}')
            print(f'    Contract:      {safe(snf.get("Contract_Status"))}')
            print(f'    Geo Tier:      {safe(snf.get("Geographic_Tier"))}')
            print(f'    Metro:         {safe(snf.get("Metro_Assignment")) or "(none)"}')
            print(f'    Address:       {safe(snf.get("Address"))}')
        else:
            print(f'  *** NO MATCHING SNF ROW IN DB ***')

        # Flag differences
        if snf:
            alf_serve = safe(alf.get('Do_We_Serve'))
            snf_serve = safe(snf.get('Do_We_Serve'))
            if alf_serve != snf_serve:
                print()
                print(f'  >>> SERVICE MISMATCH: ALF={alf_serve}, SNF={snf_serve}')

            alf_int = safe(alf.get('Integrated_Flag'))
            snf_int = safe(snf.get('Integrated_Flag'))
            alf_pcp = safe(alf.get('PCP_Flag'))
            snf_pcp = safe(snf.get('PCP_Flag'))
            alf_mh = safe(alf.get('MH_Flag'))
            snf_mh = safe(snf.get('MH_Flag'))
            if (alf_int, alf_pcp, alf_mh) != (snf_int, snf_pcp, snf_mh):
                print(f'  >>> FLAG MISMATCH: ALF=Int:{alf_int}/PCP:{alf_pcp}/MH:{alf_mh}  SNF=Int:{snf_int}/PCP:{snf_pcp}/MH:{snf_mh}')

            alf_corp = safe(alf.get('Corporate_Name'))
            snf_corp = safe(snf.get('Corporate_Name'))
            if alf_corp != snf_corp:
                print(f'  >>> CORP MISMATCH: ALF="{alf_corp}" vs SNF="{snf_corp}"')

            alf_own = safe(alf.get('Ownership_Type'))
            snf_own = safe(snf.get('Ownership_Type'))
            if alf_own != snf_own:
                print(f'  >>> OWNERSHIP MISMATCH: ALF={alf_own}, SNF={snf_own}')
        print()


if __name__ == '__main__':
    main()
