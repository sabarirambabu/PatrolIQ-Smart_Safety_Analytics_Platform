import streamlit as st
import pydeck as pdk
from utils import read_processed_csv, safe_sample

def show():
    st.title("🔥 Crime Hotspots (Cluster View)")

    df = read_processed_csv("data/crime_hotspot_clusters.csv")
    df = df.dropna(subset=["Latitude", "Longitude"])

    sample = safe_sample(df, 8000)

    # 🎨 Assign colors based on cluster
    def get_color(cluster):
        colors = [
            [255, 0, 0],    # red
            [0, 255, 0],    # green
            [0, 0, 255],    # blue
            [255, 255, 0],  # yellow
            [255, 0, 255],  # pink
            [0, 255, 255],  # cyan
        ]
        return colors[int(cluster) % len(colors)]

    sample["color"] = sample["KMeans_Cluster"].apply(get_color)

    # 🚀 PyDeck Layer
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=sample,
        get_position='[Longitude, Latitude]',
        get_color="color",
        get_radius=50,
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=sample["Latitude"].mean(),
        longitude=sample["Longitude"].mean(),
        zoom=10,
        pitch=0,
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Cluster: {KMeans_Cluster}"}
    ))

    st.write("### Cluster Distribution")
    st.bar_chart(df["KMeans_Cluster"].value_counts())