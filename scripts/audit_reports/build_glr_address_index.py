"""
build_glr_address_index.py
--------------------------
Reads the GLR Facility Dump CSV and produces a normalized address index
for dedup cross-reference. Each row is a GLR facility keyed by its
normalized address (addr_key).

Output: glr_address_index.csv in the same directory.
"""

import csv
import re
import os

# --- Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.path.join(
    os.path.expanduser("~"),
    "data-model", "reference", "GLR_Facility_Dump_2026-03-13.csv"
)
OUTPUT_CSV = os.path.join(SCRIPT_DIR, "glr_address_index.csv")

# --- Column indices (0-based) ---
COL_FACILITY_NAME = 0
COL_FACILITY_TYPE = 9
COL_STATUS = 10
COL_ADDRESS = 13
COL_CITY = 14
COL_STATE = 16
COL_ZIP = 17
COL_TOTAL_PATIENTS = 30
COL_BEDS = 51
COL_CENSUS = 52
COL_PRIMARY_CARE = 33
COL_PRIMARY_CARE_ALF = 34
COL_PRIMARY_CARE_SNF = 35
COL_PRIMARY_CARE_IL = 36
COL_PSYCHIATRY = 37
COL_PSYCHOTHERAPY = 38
COL_MENTAL_HEALTH = 40
COL_PODIATRY = 42
COL_PAIN = 44
COL_WOUND_CARE = 45
COL_SPECIALTY = 43
COL_PARENT_COMPANY = 138
COL_CMSCCN = 206

# --- Address normalization ---
SUFFIX_MAP = {
    "STREET": "ST",
    "DRIVE": "DR",
    "AVENUE": "AVE",
    "BOULEVARD": "BLVD",
    "ROAD": "RD",
    "LANE": "LN",
    "CIRCLE": "CIR",
    "COURT": "CT",
    "PLACE": "PL",
    "TRAIL": "TRL",
    # WAY stays WAY
    # Directional abbreviations
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
}


def normalize_address(raw: str) -> str:
    """Normalize a street address for matching."""
    if not raw:
        return ""
    addr = raw.strip().upper()
    # Remove periods and trailing commas
    addr = addr.replace(".", "")
    addr = addr.rstrip(",")
    # Replace suffix words
    tokens = addr.split()
    normalized_tokens = []
    for token in tokens:
        normalized_tokens.append(SUFFIX_MAP.get(token, token))
    addr = " ".join(normalized_tokens)
    # Strip trailing whitespace (already handled by split/join but be safe)
    return addr.strip()


def safe_get(row, idx):
    """Safely get a value from a row by index."""
    if idx < len(row):
        val = row[idx]
        return val.strip() if val else ""
    return ""


def main():
    rows = []

    with open(INPUT_CSV, "r", encoding="latin-1") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header

        for row in reader:
            address_raw = safe_get(row, COL_ADDRESS)
            if not address_raw:
                continue  # skip rows with no address

            addr_key = normalize_address(address_raw)
            facility_name = safe_get(row, COL_FACILITY_NAME)
            fac_type = safe_get(row, COL_FACILITY_TYPE)
            beds = safe_get(row, COL_BEDS)
            census = safe_get(row, COL_CENSUS)
            patients = safe_get(row, COL_TOTAL_PATIENTS)
            cmsccn = safe_get(row, COL_CMSCCN)
            status = safe_get(row, COL_STATUS)
            parent_company = safe_get(row, COL_PARENT_COMPANY)
            city = safe_get(row, COL_CITY)
            state = safe_get(row, COL_STATE)
            zipcode = safe_get(row, COL_ZIP)

            # Service line volumes
            pc = safe_get(row, COL_PRIMARY_CARE)
            psych = safe_get(row, COL_PSYCHIATRY)
            mh = safe_get(row, COL_MENTAL_HEALTH)
            pod = safe_get(row, COL_PODIATRY)
            pain = safe_get(row, COL_PAIN)
            wc = safe_get(row, COL_WOUND_CARE)
            spec = safe_get(row, COL_SPECIALTY)

            rows.append({
                "addr_key": addr_key,
                "glr_facility_name": facility_name,
                "glr_type": fac_type,
                "glr_beds": beds,
                "glr_census": census,
                "glr_patients": patients,
                "glr_cmsccn": cmsccn,
                "glr_status": status,
                "glr_parent_company": parent_company,
                "city": city,
                "state": state,
                "zip": zipcode,
                "pc": pc,
                "psych": psych,
                "mh": mh,
                "pod": pod,
                "pain": pain,
                "wc": wc,
                "spec": spec,
            })

    # Sort by addr_key then glr_type
    rows.sort(key=lambda r: (r["addr_key"], r["glr_type"]))

    # Write output
    fieldnames = [
        "addr_key", "glr_facility_name", "glr_type", "glr_beds",
        "glr_census", "glr_patients", "glr_cmsccn", "glr_status",
        "glr_parent_company", "city", "state", "zip",
        "pc", "psych", "mh", "pod", "pain", "wc", "spec"
    ]
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Output: {OUTPUT_CSV}")
    print(f"Total rows: {len(rows)}")


if __name__ == "__main__":
    main()
