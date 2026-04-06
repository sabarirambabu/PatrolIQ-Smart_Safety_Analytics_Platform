import streamlit as st
import pydeck as pdk
from utils import read_processed_csv, safe_sample

def show():
    st.title("🔥 Crime Hotspots (Cluster View)")

    df = read_processed_csv("data/crime_hotspot_clusters.csv")

    # ✅ CLEAN ONLY (NO DISTORTION)
    df = df.dropna(subset=["Latitude", "Longitude"])

    # Remove invalid values
    df = df[
        (df["Latitude"] != 0) &
        (df["Longitude"] != 0)
    ]

    # ✅ Keep only Chicago region (without modifying values)
    df = df[
        (df["Latitude"].between(41.5, 42.1)) &
        (df["Longitude"].between(-88, -87))
    ]

    sample = safe_sample(df, 8000)

    # 🎨 Color mapping
    def get_color(cluster):
        colors = [
            [255, 0, 0],
            [0, 255, 0],
            [0, 0, 255],
            [255, 255, 0],
            [255, 0, 255],
            [0, 255, 255],
        ]
        return colors[int(cluster) % len(colors)]

    sample["color"] = sample["KMeans_Cluster"].apply(get_color)

    # 🔥 Bigger radius = visible hotspots
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=sample,
        get_position='[Longitude, Latitude]',
        get_color="color",
        get_radius=120,   # 👈 increased
        opacity=0.6,
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=41.8781,
        longitude=-87.6298,
        zoom=10,
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Cluster: {KMeans_Cluster}"}
    ))

    st.write("### 📊 Cluster Distribution")
    st.bar_chart(df["KMeans_Cluster"].value_counts())