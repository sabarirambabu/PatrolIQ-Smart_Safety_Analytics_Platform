import streamlit as st

# Import pages
import app_pages.home as home
import app_pages.overview as overview
import app_pages.eda_analysis as eda
import app_pages.hotspot_analysis as hotspot
import app_pages.temporal_analysis as temporal
import app_pages.model_comparison as models
import app_pages.pca_visualization as pca
import app_pages.tsne_visualization as tsne

# -------------------- PAGE CONFIG -------------------- #
st.set_page_config(
    page_title="PatrolIQ Smart Safety Analytics",
    page_icon="🚔",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- STYLING -------------------- #
st.markdown("""
<style>
.stApp {background-color:#f8fafc;color:#0f172a;}
section[data-testid="stSidebar"] {background-color:#0f172a;}
div[role="radiogroup"] > label {color:#f1f5f9 !important;}
.sidebar-brand {text-align:center;font-size:40px;font-weight:700;color:white;}
.sidebar-sub {text-align:center;color:#cbd5e1;}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR -------------------- #
st.sidebar.markdown("""
<div class="sidebar-brand">🚔 PatrolIQ</div>
<div class="sidebar-sub">Smart Safety Analytics</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Go to", [
    "🏠 Home",
    "📊 Overview",
    "📈 EDA Analysis",
    "🔥 Crime Hotspots",
    "⏰ Temporal Analysis",
    "📊 Model Comparison",
    "📉 PCA",
    "🧠 t-SNE"
])

# -------------------- ROUTING -------------------- #
if page == "🏠 Home":
    home.show()

elif page == "📊 Overview":
    overview.show()

elif page == "📈 EDA Analysis":
    eda.show()

elif page == "🔥 Crime Hotspots":
    hotspot.show()

elif page == "⏰ Temporal Analysis":
    temporal.show()

elif page == "📊 Model Comparison":
    models.show()

elif page == "📉 PCA":
    pca.show()

elif page == "🧠 t-SNE":
    tsne.show()