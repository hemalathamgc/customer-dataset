import plotly.express as px


# -----------------------------------------
# Sales by Category
# -----------------------------------------
def sales_by_category_chart(df):

    data = (
        df.groupby("Category")["Purchase Amount (USD)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="Category",
        y="Purchase Amount (USD)",
        color="Purchase Amount (USD)",
        title="Sales by Category",
    )

    return fig


# -----------------------------------------
# Sales by Location
# -----------------------------------------
def sales_by_location_chart(df):

    data = (
        df.groupby("Location")["Purchase Amount (USD)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="Location",
        y="Purchase Amount (USD)",
        color="Purchase Amount (USD)",
        title="Sales by Location",
    )

    return fig


# -----------------------------------------
# Gender Distribution
# -----------------------------------------
def gender_distribution_chart(df):

    data = df["Gender"].value_counts().reset_index()
    data.columns = ["Gender", "Count"]

    fig = px.pie(
        data,
        names="Gender",
        values="Count",
        title="Gender Distribution",
        hole=0.4,
    )

    return fig


# -----------------------------------------
# Payment Method
# -----------------------------------------
def payment_method_chart(df):

    data = df["Payment Method"].value_counts().reset_index()
    data.columns = ["Payment Method", "Count"]

    fig = px.pie(
        data,
        names="Payment Method",
        values="Count",
        title="Payment Method",
        hole=0.4,
    )

    return fig


# -----------------------------------------
# Rating Distribution
# -----------------------------------------
def rating_distribution_chart(df):

    fig = px.histogram(
        df,
        x="Review Rating",
        nbins=10,
        color="Review Rating",
        title="Customer Rating Distribution",
    )

    return fig


# -----------------------------------------
# Season Sales
# -----------------------------------------
def season_sales_chart(df):

    data = (
        df.groupby("Season")["Purchase Amount (USD)"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        data,
        x="Season",
        y="Purchase Amount (USD)",
        color="Purchase Amount (USD)",
        title="Season-wise Sales",
    )

    return fig


# -----------------------------------------
# Item Purchased
# -----------------------------------------
def item_purchased_chart(df):

    data = df["Item Purchased"].value_counts().reset_index()
    data.columns = ["Item Purchased", "Count"]

    fig = px.bar(
        data,
        x="Item Purchased",
        y="Count",
        color="Count",
        title="Most Purchased Items",
    )

    return fig


# -----------------------------------------
# Age Distribution
# -----------------------------------------
def age_distribution_chart(df):

    fig = px.histogram(
        df,
        x="Age",
        nbins=15,
        color="Age",
        title="Age Distribution",
    )

    return fig


# -----------------------------------------
# Subscription Status
# -----------------------------------------
def subscription_chart(df):

    data = df["Subscription Status"].value_counts().reset_index()
    data.columns = ["Subscription Status", "Count"]

    fig = px.pie(
        data,
        names="Subscription Status",
        values="Count",
        title="Subscription Status",
        hole=0.4,
    )

    return fig


# -----------------------------------------
# Shipping Type
# -----------------------------------------
def shipping_chart(df):

    data = df["Shipping Type"].value_counts().reset_index()
    data.columns = ["Shipping Type", "Count"]

    fig = px.bar(
        data,
        x="Shipping Type",
        y="Count",
        color="Count",
        title="Shipping Type Distribution",
    )

    return fig


# -----------------------------------------
# Size Distribution
# -----------------------------------------
def size_chart(df):

    data = df["Size"].value_counts().reset_index()
    data.columns = ["Size", "Count"]

    fig = px.pie(
        data,
        names="Size",
        values="Count",
        title="Size Distribution",
        hole=0.4,
    )

    return fig


# -----------------------------------------
# Color Distribution
# -----------------------------------------
def color_chart(df):

    data = df["Color"].value_counts().reset_index()
    data.columns = ["Color", "Count"]

    fig = px.bar(
        data,
        x="Color",
        y="Count",
        color="Count",
        title="Color Distribution",
    )

    return fig


# -----------------------------------------
# Purchase Frequency
# -----------------------------------------
def frequency_chart(df):

    data = df["Frequency of Purchases"].value_counts().reset_index()
    data.columns = ["Frequency", "Count"]

    fig = px.bar(
        data,
        x="Frequency",
        y="Count",
        color="Count",
        title="Purchase Frequency",
    )

    return fig


# -----------------------------------------
# Preferred Payment Method
# -----------------------------------------
def preferred_payment_chart(df):

    data = df["Preferred Payment Method"].value_counts().reset_index()
    data.columns = ["Preferred Payment Method", "Count"]

    fig = px.pie(
        data,
        names="Preferred Payment Method",
        values="Count",
        title="Preferred Payment Method",
        hole=0.4,
    )

    return fig


# -----------------------------------------
# Discount Applied
# -----------------------------------------
def discount_chart(df):

    data = df["Discount Applied"].value_counts().reset_index()
    data.columns = ["Discount Applied", "Count"]

    fig = px.pie(
        data,
        names="Discount Applied",
        values="Count",
        title="Discount Applied",
        hole=0.4,
    )

    return fig