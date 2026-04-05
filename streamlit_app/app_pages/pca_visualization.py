import streamlit as st
import matplotlib.pyplot as plt
from utils import read_processed_csv, safe_sample

def show():
    st.title("📉 PCA Visualization")

    df = read_processed_csv("data/crime_pca_2d.csv")
    sample = safe_sample(df, 8000)

    fig, ax = plt.subplots()
    ax.scatter(sample["PCA1"], sample["PCA2"], s=5, alpha=0.5)
    st.pyplot(fig)