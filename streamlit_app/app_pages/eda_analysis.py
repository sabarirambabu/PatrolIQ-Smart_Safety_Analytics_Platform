import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import read_processed_csv, safe_sample

def show():
    st.title("📈 EDA (Exploratory Data Analysis)")

    df = read_processed_csv("data/Crime_Clean.csv")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])

    df["Hour"] = df["Date"].dt.hour
    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year

    st.metric("Total Records", len(df))

    st.subheader("Top Crime Types")
    top_crimes = df["Primary Type"].value_counts().head(10)

    fig, ax = plt.subplots()
    sns.barplot(x=top_crimes.values, y=top_crimes.index, ax=ax)
    st.pyplot(fig)

    st.subheader("Arrest Distribution")
    if "Arrest" in df.columns:
        fig, ax = plt.subplots()
        df["Arrest"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax)
        st.pyplot(fig)

    st.subheader("Hour Pattern")
    hour_trend = df["Hour"].value_counts().sort_index()

    fig, ax = plt.subplots()
    sns.barplot(x=hour_trend.index, y=hour_trend.values, ax=ax)
    st.pyplot(fig)

    st.subheader("Scatter Map")
    sample = safe_sample(df, 30000)

    fig, ax = plt.subplots()
    ax.scatter(sample["Longitude"], sample["Latitude"], s=1, alpha=0.3)
    st.pyplot(fig)