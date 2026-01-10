import pandas as pd
import os
import matplotlib.pyplot as plt


# PATH SETUP

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

MASTER_DIR = os.path.join(PROJECT_ROOT, "data", "master")
OUTPUT_CHARTS = os.path.join(PROJECT_ROOT, "outputs", "charts")

os.makedirs(OUTPUT_CHARTS, exist_ok=True)


# LOAD MASTER DATA

enroll = pd.read_csv(os.path.join(MASTER_DIR, "enrollment_all_cities.csv"))
demo = pd.read_csv(os.path.join(MASTER_DIR, "demographic_all_cities.csv"))
bio = pd.read_csv(os.path.join(MASTER_DIR, "biometric_all_cities.csv"))

# CLEAN CITY NAMES

for df in [enroll, demo, bio]:
    df["city"] = df["city"].str.replace("_", " ").str.title()

# IDENTIFY MAIN VALUE COLUMN (SAFE LOGIC)

def get_value_column(df):
    numeric_cols = df.select_dtypes("number").columns.tolist()
    return numeric_cols[0]  # first numeric column = main count

enroll_col = get_value_column(enroll)
demo_col = get_value_column(demo)
bio_col = get_value_column(bio)


#TOTAL ENROLLMENT BY CITY

enroll_sum = enroll.groupby("city")[enroll_col].sum().sort_values(ascending=False)

plt.figure()
enroll_sum.plot(kind="bar")
plt.title("Total Aadhaar Enrollment by City")
plt.xlabel("City")
plt.ylabel("Total Enrollment")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "total_enrollment_by_city.png"))
plt.close()


# BIOMETRIC UPDATES BY CITY

bio_sum = bio.groupby("city")[bio_col].sum().sort_values(ascending=False)

plt.figure()
bio_sum.plot(kind="bar")
plt.title("Total Biometric Updates by City")
plt.xlabel("City")
plt.ylabel("Biometric Updates")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "total_biometric_updates_by_city.png"))
plt.close()

#DEMOGRAPHIC UPDATES BY CITY

demo_sum = demo.groupby("city")[demo_col].sum().sort_values(ascending=False)

plt.figure()
demo_sum.plot(kind="bar")
plt.title("Total Demographic Updates by City")
plt.xlabel("City")
plt.ylabel("Demographic Updates")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "total_demographic_updates_by_city.png"))
plt.close()

# BIOMETRIC UPDATE RATE (REAL INSIGHT)

biometric_rate = (bio_sum / enroll_sum) * 1000
biometric_rate = biometric_rate.sort_values(ascending=False)

plt.figure()
biometric_rate.plot(kind="bar")
plt.title("Biometric Updates per 1000 Enrollments")
plt.xlabel("City")
plt.ylabel("Updates per 1000 Enrollments")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "biometric_update_rate.png"))
plt.close()

# DEMOGRAPHIC UPDATE RATE

demographic_rate = (demo_sum / enroll_sum) * 1000
demographic_rate = demographic_rate.sort_values(ascending=False)

plt.figure()
demographic_rate.plot(kind="bar")
plt.title("Demographic Updates per 1000 Enrollments")
plt.xlabel("City")
plt.ylabel("Updates per 1000 Enrollments")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_CHARTS, "demographic_update_rate.png"))
plt.close()

print("\nAnalysis completed successfully.")
print("Charts saved in:", OUTPUT_CHARTS)
