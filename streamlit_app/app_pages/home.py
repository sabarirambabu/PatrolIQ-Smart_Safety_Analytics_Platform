import streamlit as st

def show():

    # ---------------- GLOBAL CSS ---------------- #
    st.markdown("""
    <style>

    /* HERO GRADIENT */
    .hero {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 50px;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 18px;
        color: #cbd5e1;
    }

    /* KPI CARDS */
    .kpi {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: 0.3s;
    }

    .kpi:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }

    .kpi h2 {
        margin: 0;
        color: #0f172a;
    }

    .kpi p {
        color: #64748b;
    }

    /* FEATURE CARDS */
    .card {
        background: rgba(255,255,255,0.7);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        transition: 0.3s;
        height: 100%;
    }

    .card:hover {
        transform: scale(1.03);
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    .card h4 {
        margin-bottom: 10px;
    }

    /* CENTER TEXT */
    .center {
        text-align: center;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- HERO ---------------- #
    st.markdown("""
    <div class="hero">
        <h1>🚔 PatrolIQ</h1>
        <h3>Smart Safety Analytics Platform</h3>
        <p>Transform crime data into actionable intelligence using Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- KPI SECTION ---------------- #
    col1, col2, col3 = st.columns(3)

    col1.markdown("""
    <div class="kpi">
        <h2>📍 1M+</h2>
        <p>Crime Records</p>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown("""
    <div class="kpi">
        <h2>🔥 25+</h2>
        <p>Hotspots Identified</p>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown("""
    <div class="kpi">
        <h2>⚡ Real-time</h2>
        <p>Insights</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- FEATURES ---------------- #
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h4>🔥 Crime Hotspot Detection</h4>
            <p>Identify high-risk areas using clustering algorithms like K-Means & DBSCAN.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>⏰ Temporal Analysis</h4>
            <p>Understand crime patterns across hours, days, and months.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h4>📊 Model Comparison</h4>
            <p>Evaluate clustering models using performance metrics.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <h4>📉 Advanced Visualization</h4>
            <p>Explore PCA & t-SNE plots for deeper insights.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # ---------------- CTA ---------------- #
    st.markdown("""
    <div class="center">
        <h3>🚀 Get Started</h3>
        <p>Use the sidebar to explore insights and analytics</p>
    </div>
    """, unsafe_allow_html=True)