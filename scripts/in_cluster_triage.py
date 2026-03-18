"""
IN Cluster Triage — find suspicious same-address clusters in Indiana (V24)
"""
import openpyxl
from collections import defaultdict
import re

V24 = "C:/Users/ratwood/OneDrive - Eventus WholeHealth/Vault/02_Data_Model/Current/1_Combined_Database_FINAL_V24.xlsx"

def norm_addr(s):
    if not s:
        return ''
    s = str(s).upper().strip()
    s = re.sub(r'[.#,]', '', s)
    s = ' '.join(s.split())
    for old, new in [(' ROAD', ' RD'), (' STREET', ' ST'), (' AVENUE', ' AVE'),
                     (' BOULEVARD', ' BLVD'), (' DRIVE', ' DR'), (' LANE', ' LN'),
                     (' CIRCLE', ' CIR'), (' COURT', ' CT'), (' PLACE', ' PL'),
                     (' TRAIL', ' TRL')]:
        if s.endswith(old):
            s = s[:-len(old)] + new
    return s

wb = openpyxl.load_workbook(V24, read_only=True)
ws = wb.active

clusters = defaultdict(list)
for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
    if str(row[5] or '').strip() != 'IN':
        continue
    addr = norm_addr(row[3])
    city = str(row[4] or '').upper().strip()
    key = (addr, city)
    clusters[key].append({
        'row': i, 'type': row[0], 'name': row[1], 'addr': row[3],
        'city': row[4], 'beds': row[9], 'census': row[10],
        'served': row[11], 'corp': row[2], 'int': row[12],
        'pcp': row[13], 'mh': row[14], 'county': row[7],
        'dq_flag': row[18]
    })
wb.close()

multi = {k: v for k, v in clusters.items() if len(v) >= 2}
print(f"Total IN rows: {sum(len(v) for v in clusters.values())}")
print(f"Address clusters with 2+ rows: {len(multi)}")
print(f"Total rows in multi-clusters: {sum(len(v) for v in multi.values())}")

clean_campus = []
suspicious = []

for key, rows in sorted(multi.items()):
    type_counts = defaultdict(int)
    for r in rows:
        type_counts[r['type']] += 1
    same_type_dupes = any(c >= 2 for c in type_counts.values())
    is_suspicious = same_type_dupes or len(rows) >= 3

    if is_suspicious:
        suspicious.append((key, rows))
    else:
        clean_campus.append((key, rows))

print(f"Clean campus splits (2 rows, distinct types): {len(clean_campus)}")
print(f"Suspicious clusters (same-type dupes or 3+ rows): {len(suspicious)}")

print()
print("=" * 100)
print("SUSPICIOUS CLUSTERS — NEED REVIEW")
print("=" * 100)

for (addr, city), rows in sorted(suspicious, key=lambda x: x[0][1]):
    served_any = any(str(r['served']).upper() in ('YES', 'TRUE', 'Y') for r in rows)
    tag = ' ** SERVED **' if served_any else ''
    print(f"\n--- {addr} | {city}{tag} ({len(rows)} rows) ---")
    for r in rows:
        svc = []
        if str(r['int']).upper() in ('YES', 'TRUE', 'Y'):
            svc.append('INT')
        if str(r['pcp']).upper() in ('YES', 'TRUE', 'Y'):
            svc.append('PCP')
        if str(r['mh']).upper() in ('YES', 'TRUE', 'Y'):
            svc.append('MH')
        svc_str = '+'.join(svc) if svc else '-'
        served = 'Y' if str(r['served']).upper() in ('YES', 'TRUE', 'Y') else 'N'
        name_display = str(r['name'])[:55].ljust(55)
        beds_str = str(r['beds'] or '?').rjust(4)
        print(f"  Row {r['row']:>5}: {str(r['type']):4s} | {name_display} | beds={beds_str} | srvd={served} | svc={svc_str} | corp={r['corp']}")
