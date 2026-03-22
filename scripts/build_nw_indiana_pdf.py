#!/usr/bin/env python3
"""
Generate static PDF of NW Indiana Metro Report.
Three-tier geography, V24.1 data, Scenario 2 revenue.
"""

import sys
from collections import Counter, defaultdict
from pathlib import Path

from fpdf import FPDF

sys.path.insert(0, str(Path(__file__).resolve().parent))
from utils import safe, load_db, VAULT

V24_1 = VAULT / "Current" / "1_Combined_Database_FINAL_V24_1.xlsx"
OUTPUT = Path.home() / "Desktop" / "NW_Indiana_Metro_Report_V24_1_2026-03-18.pdf"

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
ADJ_CITIES = {'crown point','merrillville','dyer','hobart','munster','schererville','saint john','st. john','lake station','whiting','lowell','griffith','highland','cedar lake'}
VMC = {'porter','laporte','la porte'}

def classify(row):
    if safe(row.get('State')).upper()!='IN': return None
    city = safe(row.get('City')).lower()
    county = safe(row.get('County')).lower()
    metro = safe(row.get('Metro_Assignment')).lower()
    if city in CORE: return 'Core Calumet'
    if city in ADJ_CITIES or (county=='lake' and city not in CORE): return 'Lake Co. Adjacency'
    if county in VMC: return 'Val-MC Corridor'
    if metro=='northwest indiana': return 'Lake Co. Adjacency'
    return None


def sanitize(text):
    """Replace unicode chars that Helvetica can't render."""
    if not text: return ''
    return (str(text)
        .replace('\u2019', "'")  # right single quote
        .replace('\u2018', "'")  # left single quote
        .replace('\u201c', '"')  # left double quote
        .replace('\u201d', '"')  # right double quote
        .replace('\u2013', '-')  # en dash
        .replace('\u2014', '-')  # em dash
        .replace('\u2026', '...')  # ellipsis
        .replace('\u00d7', 'x')  # multiplication sign
    )

def fmt_dollar(val):
    if val >= 1_000_000:
        return f"${val/1_000_000:.2f}M"
    elif val >= 1_000:
        return f"${val/1_000:.0f}K"
    else:
        return f"${val:,.0f}"

def fmt_dollar_full(val):
    return f"${val:,.0f}"


class MetroPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return  # custom header on page 1
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 6, 'NW Indiana Metro Report | V24.1 | March 2026', align='L')
        self.cell(0, 6, f'Page {self.page_no()}', align='R', new_x="LMARGIN", new_y="NEXT")
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-12)
        self.set_font('Helvetica', 'I', 7)
        self.set_text_color(150, 150, 150)
        self.cell(0, 8, 'Eventus WholeHealth | Prepared for Sales Operations', align='C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 75, 135)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 75, 135)
        self.set_line_width(0.8)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def tier_header(self, title, r, g, b):
        self.set_fill_color(r, g, b)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, f'  {title}', fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def stat_row(self, label, value, bold=False):
        self.set_font('Helvetica', 'B' if bold else '', 9)
        self.cell(70, 5, f'  {sanitize(label)}', new_x="RIGHT")
        self.set_font('Helvetica', 'B' if bold else '', 9)
        self.cell(0, 5, sanitize(str(value)), new_x="LMARGIN", new_y="NEXT")

    def table_header(self, cols, widths):
        self.set_fill_color(0, 75, 135)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 7)
        for i, (col, w) in enumerate(zip(cols, widths)):
            align = 'R' if i >= len(cols) - 3 else 'L'
            self.cell(w, 6, col, border=1, fill=True, align=align)
        self.ln()
        self.set_text_color(0, 0, 0)

    def table_row(self, vals, widths, highlight=None):
        if highlight == 'served':
            self.set_fill_color(232, 248, 240)
            fill = True
        elif highlight == 'barrier':
            self.set_fill_color(253, 232, 232)
            fill = True
        else:
            fill = False
        self.set_font('Helvetica', '', 6.5)
        for i, (val, w) in enumerate(zip(vals, widths)):
            align = 'R' if i >= len(vals) - 3 else 'L'
            # Truncate long values
            s = sanitize(str(val))
            if len(s) > int(w / 1.8):
                s = s[:int(w / 1.8) - 1] + '..'
            self.cell(w, 5, s, border='B', fill=fill, align=align)
        self.ln()


def main():
    print("Loading V24.1...")
    headers, rows = load_db(V24_1)
    print(f"Loaded {len(rows):,} rows")

    facilities = []
    for r in rows:
        tier = classify(r)
        if not tier: continue
        cr, ir, nr, tp = calc_s2(r)
        raw_corp = safe(r.get('Corporate_Name'))
        if raw_corp.upper() in ('MAJESTIC MANAGEMENT, LLC', 'MAJESTIC MANAGEMENT LLC'):
            raw_corp = 'MAJESTIC CARE'
        try: beds = int(float(r.get('Total_Beds') or 0))
        except: beds = 0
        try: census = round(float(r.get('Census') or 0), 1)
        except: census = 0

        facilities.append({
            'name': safe(r.get('Facility_Name')),
            'type': safe(r.get('Source_Type')),
            'corp': raw_corp or '',
            'city': safe(r.get('City')),
            'beds': beds, 'census': census,
            'served': safe(r.get('Do_We_Serve','')).upper()=='YES',
            'integrated': safe(r.get('Integrated_Flag','')).upper()=='YES',
            'pcp': safe(r.get('PCP_Flag','')).upper()=='YES',
            'mh': safe(r.get('MH_Flag','')).upper()=='YES',
            'barrier': safe(r.get('Barrier','')),
            'tier': tier,
            'current_rev': round(cr),
            'integration_rev': round(ir),
            'newbiz_rev': round(nr),
        })

    def tier_stats(facs):
        t = len(facs)
        snf = sum(1 for f in facs if f['type']=='SNF')
        alf = sum(1 for f in facs if f['type']=='ALF')
        b = sum(f['beds'] for f in facs)
        c = sum(f['census'] for f in facs)
        s = sum(1 for f in facs if f['served'])
        br = sum(1 for f in facs if f['barrier'])
        cr = sum(f['current_rev'] for f in facs)
        ir = sum(f['integration_rev'] for f in facs)
        nr = sum(f['newbiz_rev'] for f in facs)
        return {'total':t,'snf':snf,'alf':alf,'beds':b,'census':c,'served':s,
                'barriers':br,'current_rev':cr,'integration_rev':ir,'newbiz_rev':nr,
                'grand_total':cr+ir+nr,
                'penetration':f"{s/t:.1%}" if t else "0%",
                'occupancy':f"{c/b:.1%}" if b else "N/A"}

    tier_order = ['Core Calumet', 'Lake Co. Adjacency', 'Val-MC Corridor']
    tier_colors = {
        'Core Calumet': (27, 79, 114),
        'Lake Co. Adjacency': (46, 134, 193),
        'Val-MC Corridor': (93, 173, 226),
    }
    tier_descs = {
        'Core Calumet': 'East Chicago, Hammond, Gary, Portage. Industrial lakeshore corridor along I-80/I-94.',
        'Lake Co. Adjacency': 'Crown Point, Merrillville, Dyer, Hobart, Munster, Schererville, Saint John, Lake Station, Whiting, Lowell. Adjacent density ring.',
        'Val-MC Corridor': 'Valparaiso, Chesterton, Michigan City, La Porte. Eastern corridor through Porter and LaPorte counties along US-20/I-94.',
    }

    tiers = {}
    for tn in tier_order:
        tiers[tn] = tier_stats([f for f in facilities if f['tier']==tn])
    tiers['Combined'] = tier_stats(facilities)

    # Build PDF
    pdf = MetroPDF(orientation='L', unit='mm', format='letter')
    pdf.set_auto_page_break(auto=True, margin=15)

    # ========== PAGE 1: Title + Summary ==========
    pdf.add_page()

    # Title block
    pdf.set_fill_color(0, 75, 135)
    pdf.rect(0, 0, pdf.w, 45, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 24)
    pdf.set_y(10)
    pdf.cell(0, 10, 'Northwest Indiana Metro Market Analysis', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', '', 12)
    pdf.cell(0, 7, 'Three-Tier Geographic Framework | Blitz Preparation for Sales Operations', align='C', new_x="LMARGIN", new_y="NEXT")
    pdf.set_font('Helvetica', 'I', 9)
    pdf.cell(0, 6, 'Data Source: V24.1 Combined Database | Revenue Model: Scenario 2 (PCP Enhanced) | March 18, 2026', align='C', new_x="LMARGIN", new_y="NEXT")

    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)

    # Combined stats bar
    c = tiers['Combined']
    pdf.set_fill_color(0, 60, 110)
    pdf.set_text_color(255, 255, 255)
    bar_y = pdf.get_y()
    pdf.rect(pdf.l_margin, bar_y, pdf.w - pdf.l_margin - pdf.r_margin, 18, 'F')

    stats_bar = [
        (f"{c['total']}", 'Facilities'),
        (f"{c['beds']:,}", 'Licensed Beds'),
        (f"{c['census']:,.0f}", 'Avg Daily Census'),
        (f"{c['served']}", 'Currently Served'),
        (f"{c['penetration']}", 'Penetration'),
        (fmt_dollar(c['grand_total']), 'Grand Total'),
    ]
    col_w = (pdf.w - pdf.l_margin - pdf.r_margin) / len(stats_bar)
    for i, (val, label) in enumerate(stats_bar):
        x = pdf.l_margin + i * col_w
        pdf.set_xy(x, bar_y + 2)
        pdf.set_font('Helvetica', 'B', 14)
        pdf.cell(col_w, 8, val, align='C')
        pdf.set_xy(x, bar_y + 10)
        pdf.set_font('Helvetica', '', 7)
        pdf.cell(col_w, 5, label.upper(), align='C')

    pdf.set_y(bar_y + 24)
    pdf.set_text_color(0, 0, 0)

    # Geographic framework
    pdf.section_title('Geographic Framework')

    for tn in tier_order:
        r, g, b = tier_colors[tn]
        t = tiers[tn]
        pdf.tier_header(tn, r, g, b)
        pdf.set_font('Helvetica', 'I', 8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 4, tier_descs[tn], new_x="LMARGIN", new_y="NEXT")
        pdf.set_text_color(0, 0, 0)
        pdf.ln(1)
        pdf.stat_row('Facilities', f"{t['total']} ({t['snf']} SNF / {t['alf']} ALF)")
        pdf.stat_row('Licensed Beds', f"{t['beds']:,}")
        pdf.stat_row('Avg Daily Census / Occupancy', f"{t['census']:,.0f} ({t['occupancy']})")
        pdf.stat_row('Served (Penetration)', f"{t['served']} ({t['penetration']})")
        pdf.stat_row('Barriers', str(t['barriers']))
        pdf.stat_row('Current Revenue', fmt_dollar_full(t['current_rev']))
        pdf.stat_row('Integration Potential', fmt_dollar_full(t['integration_rev']))
        pdf.stat_row('New Business', fmt_dollar_full(t['newbiz_rev']))
        pdf.stat_row('Grand Total', fmt_dollar_full(t['grand_total']), bold=True)
        pdf.ln(3)

    # ========== PAGE 2+: Facility Listings per Tier ==========
    fac_cols = ['Facility', 'Type', 'Corporate', 'City', 'Beds', 'Census',
                'Svc', 'Current Rev', 'Integration', 'New Business']
    fac_widths = [62, 10, 48, 28, 12, 14, 12, 28, 28, 28]

    for tn in tier_order:
        pdf.add_page()
        r, g, b = tier_colors[tn]
        pdf.section_title(f'{tn} -- Facility Listing')

        t = tiers[tn]
        pdf.set_font('Helvetica', '', 8)
        pdf.cell(0, 5,
            f"{t['total']} facilities | {t['beds']:,} beds | {t['served']} served ({t['penetration']}) | "
            f"Grand Total: {fmt_dollar_full(t['grand_total'])}",
            new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

        tier_facs = [f for f in facilities if f['tier']==tn]
        tier_facs.sort(key=lambda f: f['newbiz_rev'] + f['integration_rev'] + f['current_rev'], reverse=True)

        pdf.table_header(fac_cols, fac_widths)

        for f in tier_facs:
            if pdf.get_y() > pdf.h - 20:
                pdf.add_page()
                pdf.table_header(fac_cols, fac_widths)

            svc = []
            if f['integrated']: svc.append('INT')
            if f['pcp']: svc.append('PCP')
            if f['mh']: svc.append('MH')
            svc_str = '/'.join(svc) if svc else ''

            hl = 'barrier' if f['barrier'] else ('served' if f['served'] else None)

            pdf.table_row([
                f['name'], f['type'], f['corp'], f['city'],
                str(f['beds']), str(f['census']), svc_str,
                fmt_dollar_full(f['current_rev']),
                fmt_dollar_full(f['integration_rev']),
                fmt_dollar_full(f['newbiz_rev']),
            ], fac_widths, highlight=hl)

        # Totals
        pdf.set_font('Helvetica', 'B', 7)
        pdf.cell(fac_widths[0], 5, 'TOTAL', border='T')
        pdf.cell(fac_widths[1], 5, '', border='T')
        pdf.cell(fac_widths[2], 5, '', border='T')
        pdf.cell(fac_widths[3], 5, '', border='T')
        pdf.cell(fac_widths[4], 5, str(t['beds']), border='T', align='R')
        pdf.cell(fac_widths[5], 5, str(int(t['census'])), border='T', align='R')
        pdf.cell(fac_widths[6], 5, '', border='T')
        pdf.cell(fac_widths[7], 5, fmt_dollar_full(t['current_rev']), border='T', align='R')
        pdf.cell(fac_widths[8], 5, fmt_dollar_full(t['integration_rev']), border='T', align='R')
        pdf.cell(fac_widths[9], 5, fmt_dollar_full(t['newbiz_rev']), border='T', align='R')
        pdf.ln()

    # ========== Corporate Operators ==========
    pdf.add_page()
    pdf.section_title('Corporate Operators')

    corp_data = defaultdict(lambda: {'count':0,'beds':0,'census':0,'served':0,'cr':0,'ir':0,'nr':0,'tiers':set(),'types':set()})
    for f in facilities:
        cn = f['corp']
        if not cn or cn.upper() == 'INDEPENDENT':
            continue
        g = corp_data[cn]
        g['count']+=1; g['beds']+=f['beds']; g['census']+=f['census']
        if f['served']: g['served']+=1
        g['cr']+=f['current_rev']; g['ir']+=f['integration_rev']; g['nr']+=f['newbiz_rev']
        g['tiers'].add(f['tier']); g['types'].add(f['type'])

    corp_list = sorted(corp_data.items(), key=lambda x: x[1]['cr']+x[1]['ir']+x[1]['nr'], reverse=True)

    corp_cols = ['Corporate Name', 'Fac', 'Type', 'Beds', 'Census', 'Svd', 'Tiers', 'Current Rev', 'Integration', 'New Business']
    corp_widths = [52, 10, 12, 14, 14, 10, 42, 28, 28, 28]

    pdf.table_header(corp_cols, corp_widths)

    for name, g in corp_list:
        if pdf.get_y() > pdf.h - 20:
            pdf.add_page()
            pdf.table_header(corp_cols, corp_widths)

        types_str = '/'.join(sorted(g['types']))
        tiers_str = ', '.join(sorted(g['tiers']))

        pdf.table_row([
            name, str(g['count']), types_str, str(g['beds']),
            str(int(g['census'])), str(g['served']), tiers_str,
            fmt_dollar_full(g['cr']), fmt_dollar_full(g['ir']), fmt_dollar_full(g['nr']),
        ], corp_widths)

    # ========== Revenue Methodology ==========
    pdf.add_page()
    pdf.section_title('Revenue Methodology (Scenario 2)')

    pdf.set_font('Helvetica', '', 9)
    pdf.multi_cell(0, 5,
        'All revenue figures are derived from Economic Model Scenario 2 (PCP Enhanced) V24.1. '
        'The base formula: Annual Revenue = Average Daily Census x Per-Bed Annual Rate.\n\n'
        'Current Revenue reflects existing service relationships. '
        'Integration Potential represents additional services that could be added to currently served facilities. '
        'New Business Revenue represents full integrated package revenue from facilities not currently served. '
        'Barrier facilities show $0 for all potential revenue categories.',
        new_x="LMARGIN", new_y="NEXT")

    pdf.ln(4)

    fee_cols = ['Service Component', 'Adjuster', 'SNF Base', 'SNF Adjusted', 'ALF Base', 'ALF Adjusted']
    fee_widths = [50, 28, 24, 28, 24, 28]
    pdf.table_header(fee_cols, fee_widths)

    fee_rows = [
        ('PCP (Primary Care)', '1.00 (100%)', '$3,078', '$3,078.00', '$2,084', '$2,084.00'),
        ('MH (Mental Health)', '0.50 (50%)', '$1,211', '$605.50', '$1,431', '$715.50'),
        ('CCM (Chronic Care Mgmt)', '0.30 (30%)', '$360', '$108.00', '$360', '$108.00'),
        ('SS (Shared Savings)', '0.165 (16.5%)', '$4,800', '$792.00', '$4,800', '$792.00'),
    ]
    for row_vals in fee_rows:
        pdf.table_row(list(row_vals), fee_widths)

    pdf.set_font('Helvetica', 'B', 7)
    totals = ('Integrated Per-Bed Annual Rate', '', '', '$4,583.50', '', '$3,699.50')
    for val, w in zip(totals, fee_widths):
        pdf.cell(w, 5, val, border='T')
    pdf.ln()

    # Save
    pdf.output(str(OUTPUT))
    print(f"\nSaved: {OUTPUT}")
    print(f"Pages: {pdf.page_no()}")


if __name__ == '__main__':
    main()
