import streamlit as st


def load_css():
    st.markdown("""
    <style>

    /* Main App */
    .stApp {
        background-color: #F5F7FA;
    }

    /* Title */
    h1 {
        text-align: center;
        color: #1565C0;
        font-weight: bold;
    }

    h2,h3,h4{
        color:#0F172A;
    }

    /* KPI Cards */
    div[data-testid="stMetric"]{
        background:white;
        border-radius:15px;
        padding:20px;
        box-shadow:0px 4px 12px rgba(0,0,0,0.15);
        border-left:6px solid #1565C0;
    }

    div[data-testid="stMetricLabel"]{
        font-size:16px;
        font-weight:bold;
        color:#374151;
    }

    div[data-testid="stMetricValue"]{
        font-size:32px;
        color:#1565C0;
        font-weight:bold;
    }

    /* Sidebar */
    section[data-testid="stSidebar"]{
        background-color:#1E3A8A;
    }

    section[data-testid="stSidebar"] *{
        color:white;
    }

    /* Buttons */
    .stButton>button{
        background:#1565C0;
        color:white;
        border-radius:10px;
        border:none;
        padding:10px 18px;
        font-weight:bold;
    }

    .stButton>button:hover{
        background:#0D47A1;
        color:white;
    }

    /* Download Button */
    .stDownloadButton>button{
        background:#16A34A;
        color:white;
        border-radius:10px;
        border:none;
    }

    .stDownloadButton>button:hover{
        background:#15803D;
        color:white;
    }

    /* Dataframe */
    div[data-testid="stDataFrame"]{
        border-radius:10px;
        overflow:hidden;
    }

    </style>
    """, unsafe_allow_html=True)