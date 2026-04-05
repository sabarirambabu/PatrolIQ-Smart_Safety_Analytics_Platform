import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import read_processed_csv

def show():
    st.title("⏰ Temporal Analysis")

    df = read_processed_csv("data/Crime_Clean.csv")

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Hour"] = df["Date"].dt.hour
    df["Day"] = df["Date"].dt.day_name()

    st.line_chart(df["Hour"].value_counts().sort_index())

    pivot = pd.pivot_table(df, values="ID", index="Day", columns="Hour", aggfunc="count")

    fig, ax = plt.subplots()
    sns.heatmap(pivot, cmap="Reds", ax=ax)
    st.pyplot(fig)