import json, psycopg2
from difflib import SequenceMatcher

with open('C:/Users/ratwood/.claude/projects/C--Users-ratwood/c29c86b6-bf1d-4803-92d4-186dacf381d5/tool-results/toolu_01Vb5ahcgjgoTDFVa3mVyYZ3.json', 'r') as f:
    raw = json.load(f)
data = json.loads(raw[0]['text'])
items_raw = data['boards'][0]['groups'][0]['items_page']['items']

items = []
for item in items_raw:
    city = ''; state = ''
    for cv in item['column_values']:
        if cv['id'] == 'city__1': city = (cv['text'] or '').strip()
        if cv['id'] == 'state__1': state = (cv['text'] or '').strip()
    items.append({'id': item['id'], 'name': item['name'], 'city': city, 'state': state})

skip = {'New facility', 'new facility', 'New facility name', 'Test Facility', 'b', ''}
real = [i for i in items if i['name'] not in skip]
print(f'NFT blanks: {len(items)}, real: {len(real)}')

conn = psycopg2.connect(host='keystone-platform-postgres.postgres.database.azure.com',
    port=5432, database='postgres', user='ratwood',
    password='Ch0EeU3yz7ep5bEWTKT1UoC^NMPCZXzN', sslmode='require')
cur = conn.cursor()
cur.execute('SELECT facility_name, corporate_name_raw, city, state FROM bd.market_intel_facilities')
v25 = cur.fetchall()
cur.execute("""SELECT corporate_name FROM bd.market_intel_corporate_entities ce
    JOIN bd.market_intel_facilities f ON f.corporate_entity_id = ce.id
    GROUP BY corporate_name HAVING COUNT(*) >= 3 ORDER BY LENGTH(corporate_name) DESC""")
corporates = [r[0] for r in cur.fetchall()]
cur.close(); conn.close()
print(f'V25: {len(v25)} facilities, {len(corporates)} corporates')

state_map = {'Indiana':'IN','Ohio':'OH','Kentucky':'KY','North Carolina':'NC',
             'South Carolina':'SC','Virginia':'VA','West Virginia':'WV',
             'Georgia':'GA','Tennessee':'TN','Florida':'FL','Pennsylvania':'PA'}

def norm(s):
    if not s: return ''
    s = s.upper().strip()
    while s.endswith('(COPY)'): s = s[:-6].strip()
    for sfx in [' - SNF',' - ALF',' SNF',' ALF',' LLC',' INC',
                ' NURSING AND REHABILITATION',' NURSING & REHABILITATION',
                ' NURSING AND REHAB',' NURSING & REHAB',
                ' HEALTH AND REHABILITATION',' HEALTH & REHABILITATION',
                ' HEALTH AND REHAB',' HEALTH & REHAB',
                ' REHABILITATION CENTER',' REHAB CENTER',
                ' HEALTHCARE CENTER',' HEALTH CENTER',
                ' SENIOR LIVING',' ASSISTED LIVING',
                ' RETIREMENT COMMUNITY',' CARE CENTER',' NURSING HOME']:
        if s.endswith(sfx): s = s[:-len(sfx)].strip()
    return s

def ns(s):
    if not s: return ''
    s = s.strip()
    if len(s) == 2: return s.upper()
    return state_map.get(s, s[:2].upper())

cs = {}
for n, c, ci, st in v25:
    if ci and st:
        k = (ci.upper().strip(), st.strip())
        if k not in cs: cs[k] = []
        cs[k].append((n, c, norm(n)))
print(f'Index: {len(cs)} city+state combos')

matches = []; no_match = []
for item in real:
    iname = item['name']; icity = item['city']; istate = ns(item['state'])
    iname_n = norm(iname); iupper = iname.upper()
    result = None; method = ''
    for corp in corporates:
        if len(corp) >= 4 and corp.upper() in iupper:
            result = corp; method = 'CORP'; break
    if not result and icity and istate:
        for fn, fc, fnn in cs.get((icity.upper(), istate), []):
            if fnn == iname_n and fc:
                result = fc; method = 'EXACT'; break
    if not result and icity and istate:
        best = 0; best_corp = None
        for fn, fc, fnn in cs.get((icity.upper(), istate), []):
            if fc:
                s = SequenceMatcher(None, iname_n, fnn).ratio()
                if s > best: best = s; best_corp = fc
        if best >= 0.65: result = best_corp; method = 'FUZZY'
    if result:
        matches.append({'id': item['id'], 'name': iname, 'corporate': result, 'method': method})
    else:
        no_match.append(item)

print(f'Matched: {len(matches)}, No match: {len(no_match)}')
with open('scripts/nft_write_plan.json', 'w') as f:
    json.dump(matches, f, indent=2)
print('Saved')
