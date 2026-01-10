import pandas as pd
import glob
import os
import sys

# ABSOLUTE PATH SETUP (NO CONFUSION)
# script ka exact location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# project root (scripts se ek level upar)
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

# data folder ka exact path
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

OUTPUT_DIR = os.path.join(DATA_DIR, "master")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# MERGE FUNCTION

def merge_city_files(folder_name, output_file):
    folder_path = os.path.join(DATA_DIR, folder_name)

    print(f"\nLooking for data in: {folder_path}")

    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder not found: {folder_path}")
        sys.exit(1)

    files = glob.glob(os.path.join(folder_path, "*.csv"))

    if not files:
        print(f"[ERROR] No CSV files found in: {folder_path}")
        sys.exit(1)

    all_rows = []

    for file in files:
        filename = os.path.basename(file)

        # expected: enrollment_shahjahanpur.csv
        if "_" not in filename:
            print(f"[ERROR] Filename format wrong: {filename}")
            sys.exit(1)

        city = filename.replace(".csv", "").split("_", 1)[1]

        df = pd.read_csv(file)
        df["city"] = city

        all_rows.append(df)

    merged_df = pd.concat(all_rows, ignore_index=True)

    output_path = os.path.join(OUTPUT_DIR, output_file)
    merged_df.to_csv(output_path, index=False)

    print(f"[OK] Created → {output_path}")

# RUN MERGE

print("\nStarting merge process...")

merge_city_files("enrollment", "enrollment_all_cities.csv")
merge_city_files("demographic", "demographic_all_cities.csv")
merge_city_files("biometric", "biometric_all_cities.csv")

print("\nAll datasets merged successfully. Done.\n")
