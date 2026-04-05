import streamlit as st
import pandas as pd

def show():
    st.title("📊 Model Comparison")

    df = pd.DataFrame({
        "Algorithm": ["KMeans", "DBSCAN", "Hierarchical"],
        "Score": [0.39, 0.09, 0.38]
    })

    st.table(df)
    st.bar_chart(df.set_index("Algorithm"))