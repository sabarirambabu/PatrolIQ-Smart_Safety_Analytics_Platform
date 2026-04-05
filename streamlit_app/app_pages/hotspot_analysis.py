import streamlit as st
from utils import read_processed_csv, safe_sample

def show():
    st.title("🔥 Crime Hotspots")

    df = read_processed_csv("data/crime_hotspot_clusters.csv")
    sample = safe_sample(df, 8000)

    st.map(sample.rename(columns={"Latitude":"latitude","Longitude":"longitude"}))

    st.bar_chart(df["KMeans_Cluster"].value_counts())