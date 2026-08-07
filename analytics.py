import pandas as pd


def total_customers(df):
    """Return total unique customers."""
    if "Customer ID" in df.columns:
        return df["Customer ID"].nunique()
    return len(df)


def total_revenue(df):
    """Return total revenue."""
    if "Purchase Amount (USD)" in df.columns:
        return round(df["Purchase Amount (USD)"].sum(), 2)
    return 0


def average_purchase(df):
    """Return average purchase amount."""
    if "Purchase Amount (USD)" in df.columns:
        return round(df["Purchase Amount (USD)"].mean(), 2)
    return 0


def highest_purchase(df):
    """Return highest purchase."""
    if "Purchase Amount (USD)" in df.columns:
        return round(df["Purchase Amount (USD)"].max(), 2)
    return 0


def lowest_purchase(df):
    """Return lowest purchase."""
    if "Purchase Amount (USD)" in df.columns:
        return round(df["Purchase Amount (USD)"].min(), 2)
    return 0


def top_category(df):
    """Most popular category."""
    if "Category" in df.columns:
        return df["Category"].mode()[0]
    return "N/A"


def top_product(df):
    """Most purchased item."""
    if "Item Purchased" in df.columns:
        return df["Item Purchased"].mode()[0]
    return "N/A"


def top_location(df):
    """Location with highest sales."""
    if "Location" in df.columns:
        sales = df.groupby("Location")["Purchase Amount (USD)"].sum()
        return sales.idxmax()
    return "N/A"


def average_rating(df):
    """Average customer rating."""
    if "Review Rating" in df.columns:
        return round(df["Review Rating"].mean(), 2)
    return 0


def payment_summary(df):
    """Payment method counts."""
    if "Payment Method" in df.columns:
        return df["Payment Method"].value_counts()
    return pd.Series(dtype=int)


def category_sales(df):
    """Sales by category."""
    if (
        "Category" in df.columns
        and "Purchase Amount (USD)" in df.columns
    ):
        return (
            df.groupby("Category")["Purchase Amount (USD)"]
            .sum()
            .sort_values(ascending=False)
        )
    return pd.Series(dtype=float)


def location_sales(df):
    """Sales by location."""
    if (
        "Location" in df.columns
        and "Purchase Amount (USD)" in df.columns
    ):
        return (
            df.groupby("Location")["Purchase Amount (USD)"]
            .sum()
            .sort_values(ascending=False)
        )
    return pd.Series(dtype=float)


def season_sales(df):
    """Sales by season."""
    if (
        "Season" in df.columns
        and "Purchase Amount (USD)" in df.columns
    ):
        return (
            df.groupby("Season")["Purchase Amount (USD)"]
            .sum()
            .sort_values(ascending=False)
        )
    return pd.Series(dtype=float)


def gender_distribution(df):
    """Gender distribution."""
    if "Gender" in df.columns:
        return df["Gender"].value_counts()
    return pd.Series(dtype=int)


def rating_distribution(df):
    """Rating distribution."""
    if "Review Rating" in df.columns:
        return df["Review Rating"].value_counts().sort_index()
    return pd.Series(dtype=int)


def customer_segmentation(df):
    """
    Segment customers by purchase amount.
    """

    if "Purchase Amount (USD)" not in df.columns:
        return df

    df = df.copy()

    df["Customer Segment"] = pd.cut(
        df["Purchase Amount (USD)"],
        bins=[0, 30, 60, 100],
        labels=[
            "Low Spender",
            "Medium Spender",
            "High Spender",
        ],
    )

    return df