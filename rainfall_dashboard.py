
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Rainfall Trends in Assam",
    page_icon="🌧️",
    layout="wide"
)

# Dashboard title
st.title("Rainfall Trend Analysis in Assam")

st.write(
    "This project analyses rainfall records from the available "
    "Assam dataset to explore annual, monthly, and district-wise "
    "rainfall patterns."
)

# Load dataset
DATA_FILE = Path("Data/rainfall_assam.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)

    df["Data Acquisition Time"] = pd.to_datetime(
        df["Data Acquisition Time"],
        format="%d-%m-%Y %H:%M",
        errors="coerce"
    )

    df["Manual Daily Rainfall (mm)"] = pd.to_numeric(
        df["Manual Daily Rainfall (mm)"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "Data Acquisition Time",
            "Manual Daily Rainfall (mm)"
        ]
    )

    df["Year"] = df["Data Acquisition Time"].dt.year
    df["Month"] = df["Data Acquisition Time"].dt.month

    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

years = sorted(df["Year"].unique())

selected_years = st.sidebar.select_slider(
    "Select year range",
    options=years,
    value=(years[0], years[-1])
)

filtered_df = df[
    df["Year"].between(
        selected_years[0],
        selected_years[1]
    )
]

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric("Records analysed", f"{len(filtered_df):,}")

col2.metric(
    "Districts represented",
    filtered_df["District"].nunique()
)

col3.metric(
    "Average recorded rainfall",
    f"{filtered_df['Manual Daily Rainfall (mm)'].mean():.2f} mm"
)

# Annual analysis
st.header("Annual Rainfall Analysis")

annual = filtered_df.groupby("Year")[
    "Manual Daily Rainfall (mm)"
].mean()

fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(annual.index, annual.values, marker="o")
ax1.set_xlabel("Year")
ax1.set_ylabel("Average recorded daily rainfall (mm)")
ax1.set_title("Annual Rainfall Pattern")
ax1.grid(True, alpha=0.3)

st.pyplot(fig1)
plt.close(fig1)

# Monthly analysis
st.header("Monthly Rainfall Analysis")

monthly = filtered_df.groupby("Month")[
    "Manual Daily Rainfall (mm)"
].mean().reindex(range(1, 13))

month_names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.bar(month_names, monthly.values)
ax2.set_xlabel("Month")
ax2.set_ylabel("Average recorded daily rainfall (mm)")
ax2.set_title("Monthly Rainfall Pattern")
ax2.grid(axis="y", alpha=0.3)

st.pyplot(fig2)
plt.close(fig2)

# District analysis
st.header("District-wise Rainfall")

district = filtered_df.groupby("District")[
    "Manual Daily Rainfall (mm)"
].mean().sort_values(ascending=False)

st.bar_chart(district)

# Data table
st.header("Rainfall Records")
st.dataframe(filtered_df, use_container_width=True)

# Download filtered data
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered rainfall data",
    data=csv_data,
    file_name="assam_rainfall_data.csv",
    mime="text/csv"
)

st.caption(
    "Note: Values are averages of recorded station observations. "
    "They should not be interpreted as statewide rainfall totals."
)
