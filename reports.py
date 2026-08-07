import pandas as pd


def generate_summary(df):
    """
    Generates business summary statistics.
    """

    summary = {}

    summary["Total Customers"] = (
        df["Customer ID"].nunique()
        if "Customer ID" in df.columns
        else len(df)
    )

    summary["Total Revenue"] = (
        df["Purchase Amount"].sum()
        if "Purchase Amount" in df.columns
        else 0
    )

    summary["Average Purchase"] = (
        df["Purchase Amount"].mean()
        if "Purchase Amount" in df.columns
        else 0
    )

    if "Category" in df.columns:
        summary["Top Category"] = df["Category"].mode()[0]

    if "Product Name" in df.columns:
        summary["Top Product"] = df["Product Name"].mode()[0]

    return pd.DataFrame(
        summary.items(),
        columns=["Metric", "Value"]
    )


def export_csv(df, filename="outputs/processed_data.csv"):
    """
    Export processed dataset.
    """

    df.to_csv(filename, index=False)


def export_summary(summary_df, filename="outputs/report.csv"):
    """
    Export business summary.
    """

    summary_df.to_csv(filename, index=False)