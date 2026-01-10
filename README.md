UIDAI Hackathon – Aadhaar Data Analysis (Selected Cities)
Overview

This repository contains the code and analysis developed as part of the UIDAI Hackathon.
The project focuses on exploratory analysis of Aadhaar enrollment, biometric update, and demographic update data using a limited set of selected cities.

The objective is to understand observable patterns in workload distribution and update behavior, rather than to propose or claim any official framework or policy.

Objective

The primary goals of this project are:

To analyze Aadhaar enrollment and update activity at the city level

To compare absolute volumes with normalized update rates

To highlight differences between metropolitan and semi-urban regions

To demonstrate a clear, reproducible data analysis workflow

Data Description

Three anonymized and aggregated datasets were used:

Aadhaar Enrollment Data

Aadhaar Biometric Update Data

Aadhaar Demographic Update Data

For analysis purposes, data from selected cities was downloaded separately for each dataset.

In total:

24 CSV files (8 cities × 3 datasets)

Consolidated into 3 master datasets using Python

Note:
City selection was done purely for comparative analysis and visualization.
It does not represent any official classification or endorsement.

Methodology

The analysis followed these steps:

City-wise CSV files were organized by dataset type

All city-level files were merged into master datasets

Initial analysis focused on total activity volumes

Update rates per 1000 enrollments were calculated to normalize scale differences

Clear visualizations were generated to support interpretation

The emphasis was kept on clarity, simplicity, and explainability rather than complex modeling.

Repository Structure
uidai-aadhaar-data-analysis
│
├── scripts/
│   ├── merge_clean.py        # Merges city-wise CSV files
│   └── analysis_charts.py    # Generates charts and summaries
│
├── data/
│   └── master/               # The datasets are not included in this repository to avoid redistribution of UIDAI-provided data; only the analysis scripts and results are shared.
│
├── outputs/
│   └── charts/               # Generated charts (not uploaded)
│
└── README.md

Key Insights

Absolute enrollment and update volumes are strongly influenced by population size

Volume-based charts provide workload context but limited quality insight

Update rates per enrollment reveal operational differences across cities

Semi-urban regions tend to show higher repeat update rates compared to metros

These observations help in understanding where further review or quality improvement efforts may be useful.

Tools & Technologies

Python

Pandas

Matplotlib

GitHub

Usage

To reproduce the analysis:

Place city-wise CSV files in the appropriate dataset folders

Run the merge script:

python merge_clean.py


Run the analysis and chart generation script:

python analysis_charts.py

Disclaimer

This project is an exploratory analysis created solely for participation in the UIDAI Hackathon.
The findings are based on selected datasets and should not be interpreted as official conclusions, recommendations, or policy positions.

Author

Saksham Kumar
