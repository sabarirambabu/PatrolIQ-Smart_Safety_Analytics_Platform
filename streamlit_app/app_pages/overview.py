import streamlit as st
from utils import read_processed_csv

def show():
    st.title("📊 Crime Dataset Overview")

    df = read_processed_csv("data/Crime_Clean.csv")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", df.shape[0])
    col2.metric("Features", df.shape[1])
    col3.metric("Crime Types", df['Primary Type'].nunique())

    st.dataframe(df.head())
    st.bar_chart(df['Primary Type'].value_counts().head(10))