import streamlit as st
import pandas as pd

def show():
    st.title("📊 Model Comparison")

    df = pd.DataFrame({
        "Algorithm": ["KMeans", "DBSCAN", "Hierarchical"],
        "Score": [0.36, -0.72, 0.33]
    })

    st.table(df)
    st.bar_chart(df.set_index("Algorithm"))