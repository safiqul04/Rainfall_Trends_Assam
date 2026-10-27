
import pandas as pd
from pathlib import Path

# 1. Define the dataset location
file_path = Path("Data/rainfall_assam.csv")

# 2. Load the CSV file
df = pd.read_csv(file_path)

print("First five records:")
print(df.head())

# 3. Check dataset size
print("\nDataset shape:")
print(df.shape)

# 4. Convert observation dates into datetime format
df["Data Acquisition Time"] = pd.to_datetime(
    df["Data Acquisition Time"],
    format="%d-%m-%Y %H:%M",
    errors="coerce"
)

# 5. Convert rainfall measurements into numeric values
rainfall_column = "Manual Daily Rainfall (mm)"

df[rainfall_column] = pd.to_numeric(
    df[rainfall_column],
    errors="coerce"
)

# 6. Check missing values
print("\nMissing values:")
print(df[["Data Acquisition Time", rainfall_column]].isnull().sum())

# 7. Remove rows missing a date or rainfall measurement
df = df.dropna(
    subset=["Data Acquisition Time", rainfall_column]
)

# 8. Extract year from the observation date
df["Year"] = df["Data Acquisition Time"].dt.year

print("\nDate range:")
print(df["Data Acquisition Time"].min())
print(df["Data Acquisition Time"].max())

print("\nNumber of records after cleaning:", len(df))
print("\nData cleaning completed successfully.")


# STEP 2: Annual rainfall analysis

# Calculate average daily rainfall for each year
annual_rainfall = df.groupby("Year")[
    "Manual Daily Rainfall (mm)"
].mean()

print("\nAnnual Average Daily Rainfall (mm):")
print(annual_rainfall.round(2))

# Find the year with the highest average daily rainfall
wettest_year = annual_rainfall.idxmax()
wettest_value = annual_rainfall.max()

# Find the year with the lowest average daily rainfall
driest_year = annual_rainfall.idxmin()
driest_value = annual_rainfall.min()

print("\nYear with highest average daily rainfall:")
print(wettest_year, ":", round(wettest_value, 2), "mm/day")

print("\nYear with lowest average daily rainfall:")
print(driest_year, ":", round(driest_value, 2), "mm/day")


# STEP 3: Visualize annual rainfall

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.plot(
    annual_rainfall.index,
    annual_rainfall.values,
    marker="o",
    linestyle="-"
)

plt.title("Annual Average Daily Rainfall in Assam")
plt.xlabel("Year")
plt.ylabel("Average Recorded Daily Rainfall (mm)")
plt.grid(True)
plt.xticks(annual_rainfall.index, rotation=45)

plt.tight_layout()

# Save the graph
plt.savefig("annual_rainfall.png", dpi=300)

# Display the graph
plt.show()

print("\nAnnual rainfall graph saved successfully.")


# STEP 4: Monthly rainfall analysis

# Extract month number and month name
df["Month"] = df["Data Acquisition Time"].dt.month
df["Month_Name"] = df["Data Acquisition Time"].dt.strftime("%B")

# Calculate average recorded daily rainfall for each month
monthly_rainfall = df.groupby("Month")[
    "Manual Daily Rainfall (mm)"
].mean()

# Display the monthly results
print("\nAverage Recorded Daily Rainfall by Month:")
print(monthly_rainfall.round(2))

# Create a monthly rainfall graph
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))

plt.bar(
    monthly_rainfall.index,
    monthly_rainfall.values
)

plt.title("Average Recorded Daily Rainfall by Month in Assam")
plt.xlabel("Month")
plt.ylabel("Average Recorded Daily Rainfall (mm)")
plt.xticks(
    range(1, 13),
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

plt.savefig("monthly_rainfall.png", dpi=300)
plt.show()

print("\nMonthly rainfall graph saved successfully.")


# STEP 5: Save monthly rainfall summary

from pathlib import Path

# Create the outputs folder if it does not exist
output_folder = Path("outputs")
output_folder.mkdir(exist_ok=True)

# Convert monthly results into a DataFrame
monthly_summary = monthly_rainfall.reset_index()

monthly_summary.columns = [
    "Month",
    "Average_Rainfall_mm_per_day"
]

# Save the results
monthly_summary.to_csv(
    output_folder / "monthly_summary.csv",
    index=False
)

print("\nMonthly summary saved successfully.")
print(monthly_summary)


# STEP 6: District-wise rainfall analysis

district_column = "District"

# Check whether the district column exists
if district_column in df.columns:

    district_rainfall = df.groupby(district_column)[
        "Manual Daily Rainfall (mm)"
    ].mean().sort_values(ascending=False)

    print("\nAverage Recorded Daily Rainfall by District:")
    print(district_rainfall.round(2))

    # Save district summary
    district_summary = district_rainfall.reset_index()

    district_summary.columns = [
        "District",
        "Average_Rainfall_mm_per_day"
    ]

    district_summary.to_csv(
        output_folder / "district_summary.csv",
        index=False
    )

    print("\nDistrict summary saved successfully.")

else:
    print("District column not found. Check the dataset column names.")

