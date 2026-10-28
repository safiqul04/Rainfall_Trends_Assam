# Rainfall Trend Analysis in Assam

## 1. Project Overview

Rainfall Trend Analysis in Assam is a Python mini-project that analyses historical rainfall data to understand variations in rainfall across different years, months, and districts.

The project consists of two main Python programs:

1. **Rainfall Analysis:** Analyses the dataset and generates rainfall visualisations. 
2. **Rainfall Dashboard:** Provides an interactive interface to explore rainfall data using Streamlit.

## 2. Project Objectives

- Load and analyse rainfall data using Python.
- Inspect and clean the dataset.
- Examine missing values and data quality.
- Analyse rainfall patterns across years and months.
- Generate graphs using Matplotlib.
- Develop an interactive dashboard using Streamlit.
- Display rainfall information in a simple and understandable format.

## 3. Dataset Information

- **Dataset:** Rainfall (Manual - Daily), Assam Water Department
- **Data source:** National Water Data Portal
- **Source URL:** https://nwdp.nwic.gov.in/en/dataset/rainfall-assam-manual-daily
- **Number of records:** 28,019
- **Number of columns:** 20
- **Period covered:** 2001-2020

The dataset contains daily rainfall measurements and related information, including dates, districts, and stations.

## 4. Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit
- CSV
- Visual Studio Code

## 5. Project Folder Structure

```text
Rainfall_Trends_Assam/
├── Data/
├── notebooks/
├── outputs/
├── annual_rainfall.png
├── monthly_rainfall.png
├── rainfall_dashboard.py
└── README.md   
```

## 6. Program 1: Rainfall Analysis

**File:** `notebooks/Rainfall_analysis.py`

### Purpose

This program performs exploratory data analysis on the rainfall dataset.

### Main Activities

- Load the rainfall CSV file using Pandas.
- Examine the dataset's rows, columns, and data types.
- Check missing values and duplicate records.
- Calculate summary statistics.
- Analyse rainfall patterns across years and months.
- Generate annual and monthly rainfall graphs.
- Save or display visualisations, depending on the code configuration.

### How to Run

Open the terminal in the main project folder and execute:

```bash
python notebooks/Rainfall_analysis.py
```

Make sure the CSV file is available at the location expected by the Python script.

## 7. Program 2: Rainfall Dashboard

**File:** `rainfall_dashboard.py`

### Purpose

This program creates an interactive dashboard using Streamlit so that users can explore rainfall data through a web browser.

### Main Features

- Filter rainfall records by year range.
- Display summary metrics.
- Visualise annual rainfall patterns.
- Visualise monthly rainfall patterns.
- Explore district-wise rainfall information.
- View rainfall records in a table.
- Download filtered data as a CSV file.

### How to Run

Install the required libraries:

```bash
pip install pandas matplotlib streamlit
```

Then run the dashboard:

```bash
python -m streamlit run rainfall_dashboard.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the dashboard.

## 8. Outputs

The project includes the following visualisations:

- `annual_rainfall.png`: Annual rainfall visualisation.
- `monthly_rainfall.png`: Monthly rainfall visualisation.

The Streamlit dashboard provides additional interactive visualisations and data exploration features.

## 9. Limitations

- Some years may have incomplete or missing observations.
- District labels may have inconsistent capitalisation.
- An unusually high rainfall value of 15,240 mm requires verification against the original data source.
- The project focuses on historical analysis and visualisation; it does not currently provide a validated rainfall forecasting model.

## 10. Future Scope

- Improve data cleaning and validation.
- Add more detailed district-wise comparisons.
- Include additional reliable rainfall records.
- Improve dashboard functionality.
- Explore statistical analysis and machine learning for rainfall forecasting.

## 11. Data Source and Acknowledgement

The rainfall data used in this project is associated with the Assam Water Department and is available through the National Water Data Portal.

Source: https://nwdp.nwic.gov.in/en/dataset/rainfall-assam-manual-daily

Please check the dataset's licence and terms of use before redistributing the original data.

## 12. Author Information

**Name:** Safiqul Islam

**Name:** Din Islam Sheikh

**Programme:** B.Tech in Computer Science and Engineering

**Institution:** Assam Down Town University

**Project Title:** Rainfall Trend Analysis in Assam

## 13. Conclusion

This project demonstrates the use of Python for rainfall data analysis and visualisation. The analysis script helps examine historical data, while the Streamlit dashboard allows users to interactively explore rainfall information.

