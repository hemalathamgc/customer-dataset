import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* -----------------------------
       Main App
    ------------------------------*/

    .stApp{
        background-color:#F5F7FA;
        color:#1F2937;
        font-family:Arial, Helvetica, sans-serif;
    }

    /* -----------------------------
       Headings
    ------------------------------*/

    h1{
        color:#1565C0 !important;
        text-align:center;
        font-size:42px;
        font-weight:700;
    }

    h2{
        color:#1565C0 !important;
        font-weight:600;
    }

    h3{
        color:#0F172A !important;
        font-weight:600;
    }

    p{
        color:#374151 !important;
        font-size:16px;
    }

    /* -----------------------------
       Sidebar
    ------------------------------*/

    section[data-testid="stSidebar"]{
        background:#FFFFFF;
        border-right:2px solid #E5E7EB;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label{
        color:#111827 !important;
    }

    /* -----------------------------
       Metric Cards
    ------------------------------*/

    div[data-testid="metric-container"]{
        background:white;
        border-radius:15px;
        padding:18px;
        border:1px solid #E5E7EB;
        box-shadow:0px 3px 10px rgba(0,0,0,0.08);
    }

    div[data-testid="metric-container"] label{
        color:#6B7280 !important;
    }

    div[data-testid="metric-container"] div{
        color:#111827 !important;
    }

    /* -----------------------------
       Buttons
    ------------------------------*/

    .stButton>button{
        background:#1565C0;
        color:white;
        border:none;
        border-radius:10px;
        padding:10px 20px;
        font-weight:bold;
    }

    .stButton>button:hover{
        background:#0D47A1;
        color:white;
    }

    /* -----------------------------
       Download Button
    ------------------------------*/

    .stDownloadButton>button{
        background:#2E7D32;
        color:white;
        border:none;
        border-radius:10px;
        font-weight:bold;
    }

    .stDownloadButton>button:hover{
        background:#1B5E20;
        color:white;
    }

    /* -----------------------------
       DataFrame
    ------------------------------*/

    .stDataFrame{
        background:white;
        border-radius:10px;
        padding:10px;
    }

    /* -----------------------------
       File Uploader
    ------------------------------*/

    div[data-testid="stFileUploader"]{
        background:white;
        border:2px dashed #1565C0;
        border-radius:10px;
        padding:15px;
    }

    /* -----------------------------
       Success / Info
    ------------------------------*/

    .stAlert{
        border-radius:10px;
    }

    /* -----------------------------
       Footer
    ------------------------------*/

    footer{
        visibility:hidden;
    }

    #MainMenu{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    </style>
    """, unsafe_allow_html=True)