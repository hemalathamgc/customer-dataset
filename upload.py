import streamlit as st


def upload_dataset():
    """
    Upload CSV dataset.
    Returns uploaded file object.
    """

    uploaded_file = st.file_uploader(
        label="📂 Upload Customer Dataset (CSV)",
        type=["csv"],
        help="Upload a CSV file containing customer behavior data."
    )

    return uploaded_file