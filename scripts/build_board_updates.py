"""Generate Monday.com board update commands from V23 Excel data."""
import json

with open('/tmp/v23_entities.json', 'r') as f:
    excel = json.load(f)

board_map = {
    'ALG': (11334604808, 'ALG'),
    'Altercare': (11334620027, 'Altercare'),
    'American Senior Communities': (11334607127, 'American Senior Communities'),
    'Aom Healthcare': (11334614486, 'AOM Healthcare'),
    'Aperion Care': (11334614571, 'Aperion Care'),
    'Arbors At Ohio': (11334614521, 'Arbors'),
    'BHI Senior Living': (11334619958, 'BHI Senior Living'),
    'Brickyard Healthcare': (11334620076, 'Brickyard Healthcare'),
    'Brookdale Senior Living': (11334614445, 'Brookdale Senior Living'),
    'Carecore Health': (11334626108, 'Carecore Health'),
    'Carespring': (11334604994, 'Carespring'),
    'Caring Place Healthcare': (11334617126, 'Caring Place Healthcare'),
    'Carrolton': (11334614366, 'Carrolton'),
    'Castle Healthcare': (11334614642, 'Castle Healthcare'),
    'Cch Healthcare': (11334604806, 'CCH Healthcare'),
    'Certus Healthcare': (11334614679, 'Certus Healthcare'),
    'Choice Health Management': (11334611197, 'Choice Health Management'),
    'Ciena Healthcare/Laurel Health Care': (11334618039, 'Ciena Healthcare/Laurel Health Care'),
    'Clearview': (11334619959, 'CLEARVIEW'),
    'Consulate/Nspire/Raydiant': (11334612552, 'Avardis'),
    'Continuing Healthcare Solutions': (11334617237, 'Continuing Healthcare Solutions'),
    'Crown Healthcare Group': (11334626112, 'Crown Healthcare Group'),
    'Divine Healthcare Management': (11334626170, 'Divine Healthcare Management'),
    'Envive Healthcare': (11334626117, 'Envive Healthcare'),
    'Gardant Management Solutions': (11334604963, 'Gardant Management Solutions'),
    'HCF Management': (11334614707, 'HCF Management'),
    'Health Care Management Group': (11334614522, 'Health Care Management Group'),
    'Heritage Hall': (11334619836, 'American Healthcare LLC'),
    'Hillstone Healthcare': (11334626211, 'Hillstone Healthcare'),
    'Infinity Healthcare Consulting': (11334618176, 'Infinity Healthcare Consulting'),
    'Jag Healthcare': (11334604938, 'JAG'),
    'Kissito': (11334620081, 'Kissito Healthcare'),
    'Legacy Health Services': (11334614648, 'Legacy Health Services'),
    'Liberty Senior Living': (11334604698, 'Liberty'),
    'Life Care Centers Of America': (11334618065, 'Lifecare'),
    'Lionstone Care': (11334614394, 'Lionstone Care'),
    'Majestic Care': (11334612431, 'Majestic Care'),
    "Miller's Merry Manor": (11334611109, "Miller's Merry Manor"),
    'Momentous Health': (11334614490, 'Momentus Health'),
    'Morning Pointe Senior Living': (11334619853, 'Morning Pointe Senior Living'),
    'National Healthcare Corporation': (11334607244, 'National Healthcare Corporation'),
    'Navion': (11334614307, 'Navion'),
    'Ohio Living Communities': (11334614921, 'Ohio Living Communities'),
    'Optalis Health & Rehabilitation': (11334626111, 'Optalis Health & Rehabilitation'),
    'Otterbein Seniorlife': (11334618093, 'Otterbein Senior Life'),
    'PACS Group': (11334607147, 'PACS Group'),
    'Pavilion Healthcare': (11334612537, 'Pavilion Healthcare'),
    'Peak Resources, Inc.': (11334620025, 'Peak Resources'),
    'Phoenix Senior Living': (11334614584, 'Phoenix Senior Living'),
    'Principle Long Term Care': (11334618042, 'Principle'),
    'Priority Life Care': (11334604848, 'Priority'),
    'Progressive Quality Care': (11334605349, 'Progressive Quality Care'),
    'Pruitthealth': (11334612396, 'Pruitt Health'),
    'Saber Healthcare Group': (11334618029, 'Saber Healthcare Group'),
    'Sanstone Health & Rehabilitation': (11334614362, 'Sanstone'),
    'Seky Holding Co.': (11334614708, 'SEKY Holding Co.'),
    'Sprenger Health Care Systems': (11334620165, 'Sprenger Health Care Systems'),
    'Sunrise': (11334607158, 'Sunrise Senior Living'),
    'Terra Bella': (11334612586, 'TerraBella Senior Living'),
    'Tlc Management': (11334618092, 'TLC Management'),
    'Topaz': (11334614681, 'Topaz Healthcare'),
    'Trilogy Health Services': (11334612641, 'Trilogy'),
    'Trio Healthcare': (11334626043, 'Trio Healthcare'),
    'Vancrest Health Care Centers': (11334626141, 'Vancrest Health Care Centers'),
    'White Oak Management': (11334604910, 'White Oak Management'),
    'Windsor House, Inc.': (11334620096, 'Windsor House'),
    'Yad Healthcare': (11334605093, 'YAD'),
}

excel_by_name = {e['name']: e for e in excel}
groups = {'T1': 'topics', 'T2': 'group_mm0tm9a3', 'T3': 'group_mm0tjkkh', 'T4': 'group_mm0t6zws', 'T5': 'group_mm0t9d2z'}
tier_points = {'T1': 7, 'T2': 5, 'T3': 4, 'T4': 2, 'T5': 1}

updates = []
for board_name, (item_id, excel_name) in board_map.items():
    e = excel_by_name.get(excel_name)
    if not e:
        print(f'WARNING: No excel match for {board_name} -> {excel_name}')
        continue

    tier = e['tier']
    opp_val = e.get('total_opportunity')
    opp = f'${opp_val:,.0f}' if opp_val else ''

    col_vals = {
        'dropdown_mm0s2zdx': tier,
        'numeric_mm0syg9z': tier_points[tier],
        'numeric_mm0t1v7d': e.get('total_score') or 0,
        'numeric_mm0temf7': e.get('er') or 0,
        'numeric_mm0tv810': e.get('ir') or 0,
        'numeric_mm0tehmr': e.get('si') or 0,
        'numeric_mm0ttw6': e.get('rp') or 0,
        'numeric_mm0tcaa2': e.get('rs') or 0,
        'numeric_mm0ta5d6': e.get('ai') or 0,
        'numeric_mm0snzk8': e.get('campuses') or 0,
        'numeric_mm0tybmf': e.get('we_serve') or 0,
        'text_mm0t3m19': e.get('states') or '',
        'text_mm0t2gf0': opp,
        'text_mm0tta9b': excel_name,
    }

    if e.get('reason'):
        col_vals['text_mm0seasm'] = e['reason']
    if e.get('barrier_type'):
        col_vals['text_mm0seasm'] = str(e['barrier_type'])

    rename = excel_name if excel_name != board_name else None

    updates.append({
        'item_id': item_id,
        'board_name': board_name,
        'excel_name': excel_name,
        'tier': tier,
        'group_id': groups[tier],
        'col_vals': col_vals,
        'rename': rename,
    })

updates.sort(key=lambda x: (x['tier'], x['excel_name']))

for u in updates:
    r = f' -> {u["excel_name"]}' if u['rename'] else ''
    print(f'{u["tier"]} | {u["item_id"]} | {u["board_name"]}{r} | score={u["col_vals"]["numeric_mm0t1v7d"]}')

print(f'\nTotal updates: {len(updates)}')

with open('/tmp/board_updates.json', 'w') as f:
    json.dump(updates, f, indent=2, default=str)
