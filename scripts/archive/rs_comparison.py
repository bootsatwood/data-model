"""Side-by-side comparison: V20 Brooke RS vs V23 Tom RS.

V20: Brooke's qualitative RS from her original tiering exercise.
V23: Tom's shared savings / ACO engagement notes, coded 1-5.

This reconciliation shows where the two assessments agree and diverge."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# V20 Brooke RS scores (extracted from Final_MUO_Tiering_V20.xlsx)
# Format: entity_name: (v20_tier, v20_rs, facs, served)
V20_BROOKE = {
    # T1
    'ALG':                              ('T1', 3, 65, 65),
    'American Senior Communities':      ('T1', 5, 140, 85),
    'Brookdale Senior Living':          ('T1', 5, 58, 49),
    'CCH Healthcare':                   ('T1', 3, 39, 13),
    'Ciena Healthcare':                 ('T1', 1, 34, 1),
    'Avardis':                          ('T1', 3, 27, 12),
    'Infinity Healthcare Consulting':   ('T1', 1, 68, 38),
    'Liberty':                          ('T1', 3, 32, 8),
    'Lifecare':                         ('T1', 1, 28, 3),
    'Majestic Care':                    ('T1', 5, 37, 19),
    'National Healthcare Corp':         ('T1', 1, 16, 2),
    'Navion':                           ('T1', 3, 18, 18),
    'Otterbein Senior Life':            ('T1', 5, 16, 6),
    'PACS Group':                       ('T1', 1, 40, 1),
    'Pavilion Healthcare':              ('T1', 4, 9, 9),
    'Principle':                        ('T1', 3, 44, 17),
    'Pruitt Health':                    ('T1', 4, 27, 12),
    'Saber Healthcare Group':           ('T1', 5, 120, 58),
    'Sunrise Senior Living':            ('T1', 3, 8, 4),
    'TerraBella Senior Living':         ('T1', 3, 11, 11),
    'TLC Management':                   ('T1', 3, 33, 21),
    'Trilogy':                          ('T1', 4, 205, 23),
    # T2
    'AOM Healthcare':                   ('T2', 3, 20, 6),
    'Aperion Care':                     ('T2', 3, 12, 3),
    'Arbors':                           ('T2', 4, 16, 6),
    'BHI Senior Living':               ('T2', 1, 15, 11),
    'Brickyard Healthcare':             ('T2', 1, 23, 7),
    'Carespring':                       ('T2', 1, 15, 0),
    'Castle Healthcare':                ('T2', 3, 12, 8),
    'Clearview':                        ('T2', 1, 5, 5),
    'HCF Management':                   ('T2', 1, 15, 3),
    'American Healthcare LLC':          ('T2', 3, 16, 8),
    'JAG':                              ('T2', 3, 9, 3),
    'Kissito Healthcare':               ('T2', 1, 13, 12),
    'Lionstone Care':                   ('T2', 3, 31, 15),
    'Lutheran Services Carolinas':      ('T2', 5, 11, 9),
    'Morning Pointe Senior Living':     ('T2', 3, 24, 14),
    'Ohio Living Communities':          ('T2', 3, 11, 0),
    'Peak Resources':                   ('T2', 3, 8, 5),
    'Phoenix Senior Living':            ('T2', 1, 8, 2),
    'Priority':                         ('T2', 3, 9, 0),
    'Sanstone':                         ('T2', 3, 17, 11),
    'Southern Healthcare Mgmt':         ('T2', 1, 33, 0),  # combined Southern Assisted + Sovereign
    'Topaz Healthcare':                 ('T2', 1, 11, 11),
    'YAD':                              ('T2', 1, 8, 2),
    # T3
    'Carecore Health':                  ('T3', 1, 10, 2),
    'Trio Healthcare':                  ('T3', 1, 10, 3),
    'Caring Place Healthcare':          ('T3', 1, 10, 10),
    'Envive Healthcare':                ('T3', 1, 13, 4),
    "Miller's Merry Manor":            ('T3', 1, 14, 0),
}

# V23 Tom RS scores (from build_scoring_workbook.py TOM_RS_SCORES dict)
# Tom's annotation notes included
TOM_RS = {
    'ALG':                              (2, 'Presented SS, Charlie not interested'),
    'American Senior Communities':      (5, 'Have it on our paper, they are happy'),
    'Brookdale Senior Living':          (5, 'Have on our paper'),
    'Saber Healthcare Group':           (2, 'Not very focused, not working'),
    'Infinity Healthcare Consulting':   (2, 'Getting nowhere'),
    'Navion':                           (3, 'Good to start talking, growing'),
    'Majestic Care':                    (3, 'Expressed interest but has not gone anywhere'),
    'Pruitt Health':                    (3, 'Getting more PC, focused on own ISNP'),
    'Kisco Senior Living':              (1, 'Do not really know well'),
    'Trilogy':                          (4, 'Already covered, speaking with Dr. McNamara'),
    'Pavilion Healthcare':              (1, 'Do not really know well'),
    'Topaz Healthcare':                 (1, 'Do not really know well'),
    'Morning Pointe Senior Living':     (2, 'Not a great fit'),
    'Principle':                        (3, 'Meeting scheduled on the 17th'),
    'Liberty':                          (4, 'Gave them proposal in RFP, Liberty Advantage ISNP'),
    'TerraBella Senior Living':         (2, 'Would have to drive growth'),
    'Sanstone':                         (2, 'Presented SS, canceled meetings'),
    'Lionstone Care':                   (3, 'Tom needs to talk to Kim B'),
    'Eldercare Partners':               (3, 'Good relationship, out of KY'),
    'Otterbein Senior Life':            (1, 'Do not really know well'),
    'TLC Management':                   (3, 'Part of Hoosier Alliance, active contact'),
    'BHI Senior Living':               (1, 'All psych'),
    'Avardis':                          (2, 'Do not really know well, do not want SS'),
    'Peak Resources':                   (2, 'Not responsive or interested in SS'),
    'Arbors':                           (1, 'Do not really know well'),
    'American Healthcare LLC':          (3, 'Tom to talk to Colvin'),
    'CCH Healthcare':                   (2, 'Talk to them defensively'),
    'Lutheran Services Carolinas':      (4, 'Verbal commitment for SS'),
    'Lutheran Life Villages':           (4, 'Cathy worked with Mike for SS'),
    'Greencroft':                       (1, 'Do not really know well'),
    'Clearview':                        (3, 'In process of partnering with Telos'),
    'Priority':                         (1, 'Do not really know well'),
    'Lifecare':                         (1, 'Do not really know well'),
    'Kissito Healthcare':               (2, 'COO not interested in SS'),
    'YAD':                              (2, 'Tried but never gotten an audience'),
    'Caring Place Healthcare':          (2, 'Psych only, will not do PC'),
    'Sonida Senior Living':             (1, 'Growth opp, not doing much'),
    'Castle Healthcare':                (3, 'Brooke and Ian more involved'),
    'JAG':                              (2, 'Not much growth opp'),
    'Fundamental LTC':                  (1, 'Psych only'),
    'Cardon & Associates':              (2, 'Creating own group, Hoosier Alliance'),
    'Southern Healthcare Mgmt':         (1, 'Not in MUO Data notes'),
    'Triple Crown':                     (1, 'Not in MUO Data notes'),
    'Momentus Health':                  (1, ''),
    'Spring Arbor Management':          (1, 'Do not really know well'),
    'Cedarhurst Senior Living':         (1, 'Do not really know well'),
    'StoryPoint':                       (3, 'Part of a growth plan'),
    'Eastern Healthcare Group':         (1, 'Do not really know well'),
    'Runk & Pratt':                     (1, 'Do not really know well'),
    'MCAP':                             (1, 'Do not really know well'),
    'LifeSpire of Virginia':            (1, 'Do not really know well'),
    'Senior Lifestyle':                 (1, 'Do not really know well'),
}

# Build comparison for entities that exist in BOTH V20 and V23
print(f"{'Entity':<40} {'V20Tier':>7} {'BrookeRS':>8} {'TomRS':>6} {'Delta':>6}  Tom Notes")
print("=" * 130)

results = []
for entity, (v20_tier, brooke_rs, facs, served) in V20_BROOKE.items():
    tom_data = TOM_RS.get(entity)
    if tom_data:
        tom_rs, tom_note = tom_data
    else:
        tom_rs = 1  # default
        tom_note = '(not in Tom notes -- gap entity)'
    delta = tom_rs - brooke_rs
    results.append((entity, v20_tier, brooke_rs, tom_rs, delta, facs, served, tom_note))

# Sort by absolute delta descending
results.sort(key=lambda x: (-abs(x[4]), x[0]))

for entity, v20_tier, brooke_rs, tom_rs, delta, facs, served, tom_note in results:
    delta_str = f"{delta:+d}" if delta != 0 else " 0"
    flag = " ***" if abs(delta) >= 2 else ""
    print(f"{entity:<40} {v20_tier:>7} {brooke_rs:>8} {tom_rs:>6} {delta_str:>6}{flag}  {tom_note}")

# Summary
same = sum(1 for r in results if r[4] == 0)
tom_higher = sum(1 for r in results if r[4] > 0)
tom_lower = sum(1 for r in results if r[4] < 0)
big_delta = sum(1 for r in results if abs(r[4]) >= 2)

print()
print(f"Total entities compared: {len(results)}")
print(f"  Same score:           {same}")
print(f"  Tom scored higher:    {tom_higher}")
print(f"  Tom scored lower:     {tom_lower}")
print(f"  Big divergence (>=2): {big_delta}")

print()
print("BIG DIVERGENCES (delta >= 2):")
print("-" * 130)
for entity, v20_tier, brooke_rs, tom_rs, delta, facs, served, tom_note in results:
    if abs(delta) >= 2:
        direction = "TOM HIGHER" if delta > 0 else "TOM LOWER"
        print(f"  {entity:<38} Brooke={brooke_rs}  Tom={tom_rs}  ({direction} by {abs(delta)})  {tom_note}")
