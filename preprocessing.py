import pandas as pd


def clean_data(df):
    """
    Clean the uploaded customer shopping dataset.
    """

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Fill numeric columns with median
    numeric_columns = [
        "Age",
        "Purchase Amount (USD)",
        "Review Rating",
        "Previous Purchases",
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())

    # Fill text columns with Unknown
    text_columns = [
        "Gender",
        "Item Purchased",
        "Category",
        "Location",
        "Size",
        "Color",
        "Season",
        "Subscription Status",
        "Payment Method",
        "Shipping Type",
        "Discount Applied",
        "Promo Code Used",
        "Preferred Payment Method",
        "Frequency of Purchases",
    ]

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    # Remove invalid purchase amounts
    if "Purchase Amount (USD)" in df.columns:
        df = df[df["Purchase Amount (USD)"] >= 0]

    # Remove invalid ratings
    if "Review Rating" in df.columns:
        df = df[
            (df["Review Rating"] >= 1)
            & (df["Review Rating"] <= 5)
        ]

    return df