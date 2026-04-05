import streamlit as st
import matplotlib.pyplot as plt
from utils import read_processed_csv, safe_sample

def show():
    st.title("🧠 t-SNE Visualization")

    df = read_processed_csv("data/crime_tsne_2d.csv")
    sample = safe_sample(df, 6000)

    fig, ax = plt.subplots()
    ax.scatter(sample["TSNE1"], sample["TSNE2"], s=6, alpha=0.6)
    st.pyplot(fig)