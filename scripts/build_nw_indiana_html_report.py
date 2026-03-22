#!/usr/bin/env python3
"""
Generate HTML Metro Report for NW Indiana with Leaflet maps.
Three-tier geography, V24.1 data, Scenario 2 revenue model.
"""

import sys, json
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import safe, load_db, VAULT

V24_1 = VAULT / "Current" / "1_Combined_Database_FINAL_V24_1.xlsx"
OUTPUT = VAULT / "Current" / "Metro_Reports" / "NW_Indiana_Metro_Report_V24_1_2026-03-18.html"

# S2 Fees
FEES = {
    'SNF': {'PCP': 3078.00, 'MH_adj': 605.50, 'CCM_adj': 108.00, 'SS_adj': 792.00, 'TOTAL': 4583.50},
    'ALF': {'PCP': 2084.00, 'MH_adj': 715.50, 'CCM_adj': 108.00, 'SS_adj': 792.00, 'TOTAL': 3699.50},
}
FEES['ILF'] = FEES['ALF']

def calc_s2(row):
    st = safe(row.get('Source_Type', ''))
    fee = FEES.get(st)
    if not fee: return 0,0,0,0
    try: census = float(row.get('Census') or 0)
    except: census = 0
    served = safe(row.get('Do_We_Serve','')).upper()=='YES'
    barrier = bool(safe(row.get('Barrier','')))
    integ = safe(row.get('Integrated_Flag','')).upper()=='YES'
    pcp = safe(row.get('PCP_Flag','')).upper()=='YES'
    mh = safe(row.get('MH_Flag','')).upper()=='YES'
    cr=ir=nr=0
    if served:
        if integ: cr=census*fee['TOTAL']
        elif pcp: cr=census*(fee['PCP']+fee['CCM_adj']+fee['SS_adj'])
        elif mh: cr=census*fee['MH_adj']
        if not barrier:
            if pcp: ir=census*fee['MH_adj']
            elif mh: ir=census*(fee['PCP']+fee['CCM_adj']+fee['SS_adj'])
    else:
        if not barrier: nr=census*fee['TOTAL']
    return cr, ir, nr, ir+nr

# Geography
CORE = {'east chicago','hammond','gary','portage'}
ADJ = {'crown point','merrillville','dyer','hobart','munster','schererville','saint john','st. john','lake station','whiting','lowell','griffith','highland','cedar lake'}
VMC = {'porter','laporte','la porte'}

def classify(row):
    if safe(row.get('State')).upper()!='IN': return None
    city = safe(row.get('City')).lower()
    county = safe(row.get('County')).lower()
    metro = safe(row.get('Metro_Assignment')).lower()
    if city in CORE: return 'Core Calumet'
    if city in ADJ or (county=='lake' and city not in CORE): return 'Lake Co. Adjacency'
    if county in VMC: return 'Val-MC Corridor'
    if metro=='northwest indiana': return 'Lake Co. Adjacency'
    return None

def main():
    print("Loading V24.1...")
    headers, rows = load_db(V24_1)
    print(f"Loaded {len(rows):,} rows")

    facilities = []
    for r in rows:
        tier = classify(r)
        if not tier: continue
        cr, ir, nr, tp = calc_s2(r)
        try: lat=float(r.get('Latitude'))
        except: lat=None
        try: lon=float(r.get('Longitude'))
        except: lon=None
        try: beds=int(float(r.get('Total_Beds') or 0))
        except: beds=0
        try: census=round(float(r.get('Census') or 0),1)
        except: census=0

        # Normalize corporate name: merge known aliases
        raw_corp = safe(r.get('Corporate_Name'))
        if raw_corp.upper() in ('MAJESTIC MANAGEMENT, LLC', 'MAJESTIC MANAGEMENT LLC'):
            raw_corp = 'MAJESTIC CARE'

        facilities.append({
            'name': safe(r.get('Facility_Name')),
            'type': safe(r.get('Source_Type')),
            'corp': raw_corp or '',
            'city': safe(r.get('City')),
            'county': safe(r.get('County')),
            'zip': safe(r.get('ZIP')),
            'beds': beds, 'census': census,
            'served': safe(r.get('Do_We_Serve','')).upper()=='YES',
            'integrated': safe(r.get('Integrated_Flag','')).upper()=='YES',
            'pcp': safe(r.get('PCP_Flag','')).upper()=='YES',
            'mh': safe(r.get('MH_Flag','')).upper()=='YES',
            'barrier': safe(r.get('Barrier','')),
            'lat': lat, 'lon': lon, 'tier': tier,
            'current_rev': round(cr), 'integration_rev': round(ir),
            'newbiz_rev': round(nr), 'total_potential': round(tp),
        })

    # Compute stats per tier
    def tier_stats(facs):
        t = len(facs)
        snf = sum(1 for f in facs if f['type']=='SNF')
        alf = sum(1 for f in facs if f['type']=='ALF')
        ilf = sum(1 for f in facs if f['type']=='ILF')
        b = sum(f['beds'] for f in facs)
        c = sum(f['census'] for f in facs)
        s = sum(1 for f in facs if f['served'])
        br = sum(1 for f in facs if f['barrier'])
        cr = sum(f['current_rev'] for f in facs)
        ir = sum(f['integration_rev'] for f in facs)
        nr = sum(f['newbiz_rev'] for f in facs)
        tp = sum(f['total_potential'] for f in facs)
        return {'total':t,'snf':snf,'alf':alf,'ilf':ilf,'beds':b,'census':c,
                'served':s,'barriers':br,'current_rev':cr,
                'integration_rev':ir,'newbiz_rev':nr,'total_potential':tp,
                'grand_total':cr+tp,
                'penetration': f"{s/t:.1%}" if t else "0%",
                'occupancy': f"{c/b:.1%}" if b else "N/A"}

    tiers = {}
    for tn in ['Core Calumet','Lake Co. Adjacency','Val-MC Corridor']:
        tf = [f for f in facilities if f['tier']==tn]
        tiers[tn] = tier_stats(tf)
    tiers['Combined'] = tier_stats(facilities)

    # Corporate data (exclude independents/blanks)
    corps = defaultdict(lambda: {'count':0,'beds':0,'census':0,'served':0,'cr':0,'ir':0,'nr':0,'tp':0,'tiers':set(),'types':set()})
    for f in facilities:
        corp_name = f['corp']
        if not corp_name or corp_name == '(Independent)' or corp_name.upper() == 'INDEPENDENT':
            continue
        g = corps[corp_name]
        g['count']+=1; g['beds']+=f['beds']; g['census']+=f['census']
        if f['served']: g['served']+=1
        g['cr']+=f['current_rev']; g['ir']+=f['integration_rev']
        g['nr']+=f['newbiz_rev']; g['tp']+=f['total_potential']
        g['tiers'].add(f['tier']); g['types'].add(f['type'])

    corp_list = []
    for name, g in sorted(corps.items(), key=lambda x: x[1]['tp']+x[1]['cr'], reverse=True):
        corp_list.append({
            'name':name, 'count':g['count'], 'types':'/'.join(sorted(g['types'])),
            'beds':g['beds'], 'census':int(g['census']), 'served':g['served'],
            'tiers':list(sorted(g['tiers'])),
            'cr':g['cr'], 'ir':g['ir'], 'nr':g['nr'], 'tp':g['tp']
        })

    fac_json = json.dumps(facilities)
    corp_json = json.dumps(corp_list)
    tiers_json = json.dumps(tiers)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NW Indiana Metro Report | V24.1 | March 2026</title>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  :root {{
    --navy: #004B87;
    --core: #1B4F72;
    --adj: #2E86C1;
    --valmc: #5DADE2;
    --served: #27AE60;
    --barrier: #E74C3C;
    --bg: #F8F9FA;
    --card: #FFFFFF;
    --text: #2C3E50;
    --muted: #7F8C8D;
    --border: #DEE2E6;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; background: var(--bg); color: var(--text); line-height: 1.5; }}

  .header {{ background: linear-gradient(135deg, var(--navy) 0%, var(--core) 100%); color: white; padding: 40px 0; }}
  .header-inner {{ max-width: 1200px; margin: 0 auto; padding: 0 24px; }}
  .header h1 {{ font-size: 28px; font-weight: 700; margin-bottom: 6px; }}
  .header .subtitle {{ font-size: 15px; opacity: 0.85; }}
  .header .meta {{ display: flex; gap: 24px; margin-top: 16px; font-size: 13px; opacity: 0.7; }}

  .container {{ max-width: 1200px; margin: 0 auto; padding: 24px; }}

  .section {{ margin-bottom: 40px; }}
  .section-title {{ font-size: 22px; font-weight: 700; color: var(--navy); margin-bottom: 16px; padding-bottom: 8px; border-bottom: 3px solid var(--navy); }}

  .card {{ background: var(--card); border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); padding: 24px; margin-bottom: 20px; }}

  .tier-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 20px; }}
  @media (max-width: 900px) {{ .tier-grid {{ grid-template-columns: 1fr; }} }}

  .tier-card {{ border-radius: 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }}
  .tier-card .tier-header {{ padding: 14px 20px; color: white; font-weight: 700; font-size: 15px; }}
  .tier-card .tier-body {{ padding: 20px; background: white; }}
  .tier-card .tier-body .stat {{ display: flex; justify-content: space-between; padding: 6px 0; border-bottom: 1px solid var(--border); font-size: 14px; }}
  .tier-card .tier-body .stat:last-child {{ border-bottom: none; }}
  .tier-card .tier-body .stat .label {{ color: var(--muted); }}
  .tier-card .tier-body .stat .value {{ font-weight: 600; }}
  .tier-card .tier-body .stat.highlight .value {{ color: var(--navy); font-size: 16px; }}

  .combined-bar {{ background: var(--navy); color: white; border-radius: 8px; padding: 20px 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; }}
  .combined-bar .cb-stat {{ text-align: center; }}
  .combined-bar .cb-stat .cb-val {{ font-size: 24px; font-weight: 700; }}
  .combined-bar .cb-stat .cb-label {{ font-size: 12px; opacity: 0.7; text-transform: uppercase; letter-spacing: 0.5px; }}

  .map-container {{ height: 500px; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }}

  .geo-desc {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 20px; }}
  @media (max-width: 900px) {{ .geo-desc {{ grid-template-columns: 1fr; }} }}
  .geo-desc .geo-item {{ padding: 16px; border-radius: 8px; border-left: 4px solid; background: white; }}
  .geo-desc .geo-item h4 {{ margin-bottom: 6px; font-size: 14px; }}
  .geo-desc .geo-item p {{ font-size: 13px; color: var(--muted); line-height: 1.5; }}

  .legend {{ display: flex; gap: 20px; flex-wrap: wrap; padding: 12px 16px; background: white; border-radius: 8px; margin-bottom: 12px; font-size: 13px; }}
  .legend-item {{ display: flex; align-items: center; gap: 6px; }}
  .legend-dot {{ width: 14px; height: 14px; border-radius: 50%; }}

  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th {{ background: var(--navy); color: white; padding: 10px 12px; text-align: left; font-weight: 600; position: sticky; top: 0; }}
  td {{ padding: 8px 12px; border-bottom: 1px solid var(--border); }}
  tr:hover td {{ background: #F0F6FF; }}
  tr.served td {{ background: #E8F8F0; }}
  tr.barrier td {{ background: #FDE8E8; }}
  .table-wrap {{ max-height: 600px; overflow-y: auto; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }}
  .currency {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .num {{ text-align: right; }}

  .tab-bar {{ display: flex; gap: 4px; margin-bottom: 0; }}
  .tab-btn {{ padding: 10px 20px; border: none; background: var(--border); cursor: pointer; border-radius: 8px 8px 0 0; font-size: 13px; font-weight: 600; color: var(--muted); }}
  .tab-btn.active {{ background: var(--navy); color: white; }}
  .tab-content {{ display: none; }}
  .tab-content.active {{ display: block; }}

  .methodology {{ font-size: 13px; color: var(--muted); line-height: 1.7; }}
  .methodology table {{ margin: 12px 0; }}
  .methodology th {{ background: #6C757D; font-size: 12px; }}
  .methodology td {{ font-size: 12px; }}

  .footer {{ text-align: center; padding: 24px; color: var(--muted); font-size: 12px; border-top: 1px solid var(--border); margin-top: 40px; }}

  .filter-bar {{ display: flex; gap: 8px; margin-bottom: 12px; flex-wrap: wrap; }}
  .filter-btn {{ padding: 6px 14px; border: 2px solid var(--border); background: white; cursor: pointer; border-radius: 20px; font-size: 12px; font-weight: 600; }}
  .filter-btn.active {{ border-color: var(--navy); background: var(--navy); color: white; }}
</style>
</head>
<body>

<div class="header">
  <div class="header-inner">
    <h1>Northwest Indiana Metro Market Analysis</h1>
    <div class="subtitle">Three-Tier Geographic Framework | Blitz Preparation for Sales Operations</div>
    <div class="meta">
      <span>Data Source: V24.1 Combined Database (25,583 rows)</span>
      <span>Revenue Model: Scenario 2 (PCP Enhanced)</span>
      <span>Generated: March 18, 2026</span>
    </div>
  </div>
</div>

<div class="container">

  <!-- Combined Bar -->
  <div class="combined-bar" style="margin-bottom: 32px; margin-top: -8px;">
    <div class="cb-stat"><div class="cb-val">{tiers['Combined']['total']}</div><div class="cb-label">Facilities</div></div>
    <div class="cb-stat"><div class="cb-val">{tiers['Combined']['beds']:,}</div><div class="cb-label">Licensed Beds</div></div>
    <div class="cb-stat"><div class="cb-val">{tiers['Combined']['census']:,.0f}</div><div class="cb-label">Avg Daily Census</div></div>
    <div class="cb-stat"><div class="cb-val">{tiers['Combined']['served']}</div><div class="cb-label">Currently Served</div></div>
    <div class="cb-stat"><div class="cb-val">{tiers['Combined']['penetration']}</div><div class="cb-label">Penetration</div></div>
    <div class="cb-stat"><div class="cb-val">${tiers['Combined']['grand_total']:,.0f}</div><div class="cb-label">Grand Total Revenue</div></div>
  </div>

  <!-- Geography Section -->
  <div class="section">
    <div class="section-title">Geographic Framework</div>

    <div class="geo-desc">
      <div class="geo-item" style="border-color: var(--core);">
        <h4 style="color: var(--core);">Tier 1: Core Calumet</h4>
        <p>East Chicago, Hammond, Gary, Portage. The industrial lakeshore corridor along I-80/I-94 at the southern tip of Lake Michigan. Ian's scoped blitz geography.</p>
      </div>
      <div class="geo-item" style="border-color: var(--adj);">
        <h4 style="color: var(--adj);">Tier 2: Lake County Adjacency</h4>
        <p>Crown Point, Merrillville, Dyer, Hobart, Munster, Schererville, Saint John, Lake Station, Whiting, Lowell. Adjacent density surrounding the core, within the original 15-mile Calumet radius.</p>
      </div>
      <div class="geo-item" style="border-color: var(--valmc);">
        <h4 style="color: var(--valmc);">Tier 3: Val-MC Corridor</h4>
        <p>Valparaiso, Chesterton, Michigan City, La Porte. The eastern corridor through Porter and LaPorte counties along US-20 and I-94. Entirely within Indiana.</p>
      </div>
    </div>

    <div class="legend">
      <div class="legend-item"><div class="legend-dot" style="background: var(--core);"></div> Core Calumet</div>
      <div class="legend-item"><div class="legend-dot" style="background: var(--adj);"></div> Lake Co. Adjacency</div>
      <div class="legend-item"><div class="legend-dot" style="background: var(--valmc);"></div> Val-MC Corridor</div>
      <div class="legend-item"><div class="legend-dot" style="background: var(--served); border: 2px solid #1E8449;"></div> Currently Served</div>
      <div class="legend-item"><div class="legend-dot" style="background: var(--barrier);"></div> Barrier</div>
    </div>

    <div id="map-main" class="map-container"></div>
  </div>

  <!-- Tier Summaries -->
  <div class="section">
    <div class="section-title">Market Summary by Tier</div>
    <div class="tier-grid" id="tier-cards"></div>
  </div>

  <!-- Density Maps -->
  <div class="section">
    <div class="section-title">Facility Density by Revenue Potential</div>
    <p style="font-size:13px; color: var(--muted); margin-bottom: 12px;">Circle size proportional to Total Potential Revenue. Larger circles represent greater growth opportunity.</p>
    <div id="map-density" class="map-container"></div>
  </div>

  <!-- Facility Listings -->
  <div class="section">
    <div class="section-title">Complete Facility Listings</div>
    <div class="filter-bar" id="tier-filters">
      <button class="filter-btn active" data-tier="all">All ({tiers['Combined']['total']})</button>
      <button class="filter-btn" data-tier="Core Calumet">Core Calumet ({tiers['Core Calumet']['total']})</button>
      <button class="filter-btn" data-tier="Lake Co. Adjacency">Lake Co. Adjacency ({tiers['Lake Co. Adjacency']['total']})</button>
      <button class="filter-btn" data-tier="Val-MC Corridor">Val-MC Corridor ({tiers['Val-MC Corridor']['total']})</button>
      <button class="filter-btn" data-tier="served">Served Only ({tiers['Combined']['served']})</button>
    </div>
    <div class="table-wrap">
      <table id="fac-table">
        <thead>
          <tr>
            <th>Facility</th><th>Type</th><th>Corporate</th><th>City</th>
            <th>Tier</th><th class="num">Beds</th><th class="num">Census</th>
            <th>Served</th><th>INT</th><th>PCP</th><th>MH</th>
            <th class="currency">Current Rev</th><th class="currency">Integration</th><th class="currency">New Business</th>
          </tr>
        </thead>
        <tbody id="fac-tbody"></tbody>
      </table>
    </div>
  </div>

  <!-- Corporate Operators -->
  <div class="section">
    <div class="section-title">Corporate Operators</div>
    <p style="font-size:13px; color: var(--muted); margin-bottom: 12px;">Sorted by combined revenue opportunity (Current + Total Potential). Click column headers to re-sort.</p>
    <div class="table-wrap">
      <table id="corp-table">
        <thead>
          <tr>
            <th>Corporate Name</th><th class="num">Facilities</th><th>Type</th>
            <th class="num">Beds</th><th class="num">Census</th><th class="num">Served</th>
            <th>Tiers</th><th class="currency">Current Rev</th><th class="currency">Integration</th><th class="currency">New Business</th>
          </tr>
        </thead>
        <tbody id="corp-tbody"></tbody>
      </table>
    </div>
  </div>

  <!-- Revenue Methodology -->
  <div class="section">
    <div class="section-title">Revenue Methodology (Scenario 2)</div>
    <div class="card methodology">
      <p>All revenue figures are derived from Economic Model Scenario 2 (PCP Enhanced) V24.1. The base formula:</p>
      <p style="text-align:center; font-weight:600; margin: 12px 0;">Annual Revenue = Average Daily Census &times; Per-Bed Annual Rate</p>
      <table>
        <thead>
          <tr><th>Service Component</th><th>Adjuster</th><th>SNF Base</th><th>SNF Adjusted</th><th>ALF Base</th><th>ALF Adjusted</th></tr>
        </thead>
        <tbody>
          <tr><td>PCP (Primary Care)</td><td>1.00 (100%)</td><td>$3,078</td><td>$3,078.00</td><td>$2,084</td><td>$2,084.00</td></tr>
          <tr><td>MH (Mental Health)</td><td>0.50 (50%)</td><td>$1,211</td><td>$605.50</td><td>$1,431</td><td>$715.50</td></tr>
          <tr><td>CCM (Chronic Care Mgmt)</td><td>0.30 (30%)</td><td>$360</td><td>$108.00</td><td>$360</td><td>$108.00</td></tr>
          <tr><td>SS (Shared Savings)</td><td>0.165 (16.5%)</td><td>$4,800</td><td>$792.00</td><td>$4,800</td><td>$792.00</td></tr>
          <tr style="font-weight:600;"><td>Integrated Per-Bed Annual Rate</td><td></td><td></td><td>$4,583.50</td><td></td><td>$3,699.50</td></tr>
        </tbody>
      </table>
      <p style="margin-top:12px;">Current Revenue reflects existing service relationships. Total Potential Revenue = Integration Revenue (upsell to served) + New Business Revenue (full package to unserved, no barrier). Barrier facilities show $0 potential.</p>
    </div>
  </div>

</div>

<div class="footer">
  Eventus WholeHealth &bull; NW Indiana Metro Report &bull; V24.1 &bull; March 2026 &bull; Prepared for Sales Operations
</div>

<script>
const facilities = {fac_json};
const corps = {corp_json};
const tiers = {tiers_json};

const COLORS = {{
  'Core Calumet': '#1B4F72',
  'Lake Co. Adjacency': '#2E86C1',
  'Val-MC Corridor': '#5DADE2'
}};

// --- Tier Summary Cards ---
(function() {{
  const container = document.getElementById('tier-cards');
  const tierOrder = ['Core Calumet', 'Lake Co. Adjacency', 'Val-MC Corridor'];
  const tierLabels = {{
    'Core Calumet': 'Core Calumet',
    'Lake Co. Adjacency': 'Lake Co. Adjacency',
    'Val-MC Corridor': 'Val-MC Corridor'
  }};

  tierOrder.forEach(tn => {{
    const t = tiers[tn];
    const color = COLORS[tn];
    const card = document.createElement('div');
    card.className = 'tier-card';
    card.innerHTML = `
      <div class="tier-header" style="background: ${{color}};">${{tierLabels[tn]}}</div>
      <div class="tier-body">
        <div class="stat highlight"><span class="label">Facilities</span><span class="value">${{t.total}} (${{t.snf}} SNF / ${{t.alf}} ALF${{t.ilf ? ' / '+t.ilf+' ILF' : ''}})</span></div>
        <div class="stat"><span class="label">Licensed Beds</span><span class="value">${{t.beds.toLocaleString()}}</span></div>
        <div class="stat"><span class="label">Avg Daily Census</span><span class="value">${{Math.round(t.census).toLocaleString()}}</span></div>
        <div class="stat"><span class="label">Occupancy</span><span class="value">${{t.occupancy}}</span></div>
        <div class="stat"><span class="label">Served</span><span class="value">${{t.served}} (${{t.penetration}})</span></div>
        <div class="stat"><span class="label">Barriers</span><span class="value">${{t.barriers}}</span></div>
        <div class="stat"><span class="label">Current Revenue</span><span class="value">$${{t.current_rev.toLocaleString()}}</span></div>
        <div class="stat"><span class="label">Integration Potential</span><span class="value">$${{t.integration_rev.toLocaleString()}}</span></div>
        <div class="stat"><span class="label">New Business</span><span class="value">$${{t.newbiz_rev.toLocaleString()}}</span></div>
        <div class="stat highlight"><span class="label">Grand Total</span><span class="value">$${{t.grand_total.toLocaleString()}}</span></div>
      </div>
    `;
    container.appendChild(card);
  }});
}})();

// --- Main Map ---
(function() {{
  const map = L.map('map-main').setView([41.52, -87.15], 10);
  L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
    attribution: '&copy; OpenStreetMap contributors',
    maxZoom: 18
  }}).addTo(map);

  facilities.forEach(f => {{
    if (!f.lat || !f.lon) return;
    const color = f.barrier ? '#E74C3C' : (f.served ? '#27AE60' : COLORS[f.tier]);
    const radius = f.served ? 8 : (f.barrier ? 7 : 6);
    const marker = L.circleMarker([f.lat, f.lon], {{
      radius: radius,
      fillColor: color,
      color: f.served ? '#1E8449' : '#333',
      weight: f.served ? 2 : 1,
      opacity: 0.9,
      fillOpacity: 0.8
    }}).addTo(map);

    const status = f.barrier ? '<span style="color:#E74C3C;font-weight:700;">BARRIER: '+f.barrier+'</span>' :
                   (f.served ? '<span style="color:#27AE60;font-weight:700;">SERVED</span>' :
                   '<span style="color:#7F8C8D;">Available</span>');
    const svcFlags = [f.integrated?'INT':'', f.pcp?'PCP':'', f.mh?'MH':''].filter(Boolean).join(', ') || '-';

    marker.bindPopup(`
      <div style="min-width:220px;">
        <div style="font-weight:700;font-size:14px;margin-bottom:4px;">${{f.name}}</div>
        <div style="font-size:12px;color:#7F8C8D;margin-bottom:8px;">${{f.corp}}</div>
        <table style="font-size:12px;width:100%;">
          <tr><td>Type</td><td style="text-align:right;font-weight:600;">${{f.type}}</td></tr>
          <tr><td>City</td><td style="text-align:right;">${{f.city}}</td></tr>
          <tr><td>Tier</td><td style="text-align:right;">${{f.tier}}</td></tr>
          <tr><td>Beds / Census</td><td style="text-align:right;">${{f.beds}} / ${{f.census}}</td></tr>
          <tr><td>Services</td><td style="text-align:right;">${{svcFlags}}</td></tr>
          <tr><td>Status</td><td style="text-align:right;">${{status}}</td></tr>
          <tr><td>Current Rev</td><td style="text-align:right;font-weight:600;">$${{f.current_rev.toLocaleString()}}</td></tr>
          <tr><td>Integration</td><td style="text-align:right;">$${{f.integration_rev.toLocaleString()}}</td></tr>
          <tr><td>New Business</td><td style="text-align:right;">$${{f.newbiz_rev.toLocaleString()}}</td></tr>
        </table>
      </div>
    `);
  }});
}})();

// --- Density Map ---
(function() {{
  const map = L.map('map-density').setView([41.52, -87.15], 10);
  L.tileLayer('https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}@2x.png', {{
    attribution: '&copy; OpenStreetMap &copy; CARTO',
    maxZoom: 18
  }}).addTo(map);

  const maxPot = Math.max(...facilities.map(f => f.total_potential + f.current_rev));

  // Sort so smaller circles render on top
  const sorted = [...facilities].sort((a,b) => (b.total_potential+b.current_rev) - (a.total_potential+a.current_rev));

  sorted.forEach(f => {{
    if (!f.lat || !f.lon) return;
    const rev = f.total_potential + f.current_rev;
    const r = Math.max(4, Math.sqrt(rev / maxPot) * 35);
    const color = COLORS[f.tier];

    L.circleMarker([f.lat, f.lon], {{
      radius: r,
      fillColor: color,
      color: color,
      weight: 1,
      opacity: 0.7,
      fillOpacity: 0.35
    }}).addTo(map).bindPopup(
      `<strong>${{f.name}}</strong><br>${{f.type}} | ${{f.city}}<br>` +
      `Beds: ${{f.beds}} | Census: ${{f.census}}<br>` +
      `<strong>Grand Total: $${{rev.toLocaleString()}}</strong>`
    );
  }});
}})();

// --- Facility Table ---
function renderFacTable(filter) {{
  const tbody = document.getElementById('fac-tbody');
  let data = [...facilities];

  if (filter === 'served') data = data.filter(f => f.served);
  else if (filter !== 'all') data = data.filter(f => f.tier === filter);

  data.sort((a,b) => (b.total_potential + b.current_rev) - (a.total_potential + a.current_rev));

  tbody.innerHTML = data.map(f => {{
    const cls = f.barrier ? 'barrier' : (f.served ? 'served' : '');
    return `<tr class="${{cls}}">
      <td>${{f.name}}</td><td>${{f.type}}</td><td>${{f.corp}}</td><td>${{f.city}}</td>
      <td>${{f.tier}}</td><td class="num">${{f.beds}}</td><td class="num">${{f.census}}</td>
      <td>${{f.served?'Yes':''}}</td><td>${{f.integrated?'Yes':''}}</td><td>${{f.pcp?'Yes':''}}</td><td>${{f.mh?'Yes':''}}</td>
      <td class="currency">$${{f.current_rev.toLocaleString()}}</td>
      <td class="currency">$${{f.integration_rev.toLocaleString()}}</td>
      <td class="currency">$${{f.newbiz_rev.toLocaleString()}}</td>
    </tr>`;
  }}).join('');
}}

document.querySelectorAll('#tier-filters .filter-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('#tier-filters .filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    renderFacTable(btn.dataset.tier);
  }});
}});

renderFacTable('all');

// --- Corporate Table ---
(function() {{
  const tbody = document.getElementById('corp-tbody');
  tbody.innerHTML = corps.map(c => `
    <tr>
      <td>${{c.name}}</td><td class="num">${{c.count}}</td><td>${{c.types}}</td>
      <td class="num">${{c.beds}}</td><td class="num">${{c.census}}</td><td class="num">${{c.served}}</td>
      <td>${{c.tiers.join(', ')}}</td>
      <td class="currency">$${{c.cr.toLocaleString()}}</td>
      <td class="currency">$${{c.ir.toLocaleString()}}</td>
      <td class="currency">$${{c.nr.toLocaleString()}}</td>
    </tr>
  `).join('');
}})();
</script>

</body>
</html>"""

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"\nSaved: {OUTPUT}")
    print(f"Facilities: {len(facilities)}")
    print(f"File size: {OUTPUT.stat().st_size / 1024:.0f} KB")


if __name__ == '__main__':
    main()
