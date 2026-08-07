import streamlit as st
import pandas as pd

from upload import upload_dataset
from preprocessing import clean_data
from styles import load_css

from analytics import (
    total_customers,
    total_revenue,
    average_purchase,
    highest_purchase,
    top_category,
    top_product,
    top_location,
    average_rating,
)

from visualization import (
    sales_by_category_chart,
    sales_by_location_chart,
    gender_distribution_chart,
    payment_method_chart,
    rating_distribution_chart,
    season_sales_chart,
    item_purchased_chart,
    age_distribution_chart,
    subscription_chart,
    shipping_chart,
    size_chart,
    color_chart,
    frequency_chart,
    preferred_payment_chart,
    discount_chart,
)

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="Customer Behavior Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)

load_css()

st.title("📊 Customer Behavior Analytics Dashboard")
st.markdown("---")

# -------------------------------------------------------
# UPLOAD DATASET
# -------------------------------------------------------

uploaded_file = upload_dataset()

if uploaded_file is not None:

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Show uploaded data
    st.subheader("📁 Uploaded Dataset")
    st.dataframe(df, use_container_width=True)

    # Clean Dataset
    if st.button("🧹 Clean Dataset"):
        df = clean_data(df)
        st.success("Dataset cleaned successfully!")

    # -------------------------------------------------------
    # SIDEBAR FILTERS
    # -------------------------------------------------------

    st.sidebar.header("🎯 Dashboard Filters")

    if "Gender" in df.columns:
        gender = st.sidebar.multiselect(
            "Gender",
            sorted(df["Gender"].dropna().unique()),
            default=sorted(df["Gender"].dropna().unique()),
        )
        df = df[df["Gender"].isin(gender)]

    if "Category" in df.columns:
        category = st.sidebar.multiselect(
            "Category",
            sorted(df["Category"].dropna().unique()),
            default=sorted(df["Category"].dropna().unique()),
        )
        df = df[df["Category"].isin(category)]

    if "Location" in df.columns:
        location = st.sidebar.multiselect(
            "Location",
            sorted(df["Location"].dropna().unique()),
            default=sorted(df["Location"].dropna().unique()),
        )
        df = df[df["Location"].isin(location)]

    if "Season" in df.columns:
        season = st.sidebar.multiselect(
            "Season",
            sorted(df["Season"].dropna().unique()),
            default=sorted(df["Season"].dropna().unique()),
        )
        df = df[df["Season"].isin(season)]

    if "Payment Method" in df.columns:
        payment = st.sidebar.multiselect(
            "Payment Method",
            sorted(df["Payment Method"].dropna().unique()),
            default=sorted(df["Payment Method"].dropna().unique()),
        )
        df = df[df["Payment Method"].isin(payment)]
            # -------------------------------------------------------
    # DASHBOARD OVERVIEW
    # -------------------------------------------------------

    st.markdown("---")
    st.subheader("📈 Dashboard Overview")

    row1_col1, row1_col2, row1_col3, row1_col4 = st.columns(4)

    with row1_col1:
        st.metric(
            "👥 Total Customers",
            total_customers(df)
        )

    with row1_col2:
        st.metric(
            "💰 Total Revenue",
            f"${total_revenue(df):,.2f}"
        )

    with row1_col3:
        st.metric(
            "🛒 Average Purchase",
            f"${average_purchase(df):,.2f}"
        )

    with row1_col4:
        st.metric(
            "📈 Highest Purchase",
            f"${highest_purchase(df):,.2f}"
        )

    # -------------------------------------------------------
    # SECOND KPI ROW
    # -------------------------------------------------------

    row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

    with row2_col1:
        st.metric(
            "🏷 Top Category",
            top_category(df) if "Category" in df.columns else "N/A"
        )

    with row2_col2:
        st.metric(
            "🛍 Top Product",
            top_product(df) if "Item Purchased" in df.columns else "N/A"
        )

    with row2_col3:
        st.metric(
            "📍 Top Location",
            top_location(df) if "Location" in df.columns else "N/A"
        )

    with row2_col4:
        st.metric(
            "⭐ Average Rating",
            average_rating(df) if "Review Rating" in df.columns else "N/A"
        )

    # -------------------------------------------------------
    # THIRD KPI ROW
    # -------------------------------------------------------

    category_count = df["Category"].nunique() if "Category" in df.columns else 0
    location_count = df["Location"].nunique() if "Location" in df.columns else 0
    payment_count = (
        df["Payment Method"].nunique()
        if "Payment Method" in df.columns
        else 0
    )

    row3_col1, row3_col2, row3_col3 = st.columns(3)

    with row3_col1:
        st.metric(
            "📦 Categories",
            category_count
        )

    with row3_col2:
        st.metric(
            "🌍 Locations",
            location_count
        )

    with row3_col3:
        st.metric(
            "💳 Payment Methods",
            payment_count
        )

    # -------------------------------------------------------
    # BUSINESS INSIGHTS
    # -------------------------------------------------------

    st.markdown("---")
    st.subheader("📊 Business Insights")

    insight1, insight2 = st.columns(2)

    with insight1:

        st.success(
            f"""
### 🏆 Key Highlights

📦 Top Category :
**{top_category(df) if 'Category' in df.columns else 'N/A'}**

🛍 Top Product :
**{top_product(df) if 'Item Purchased' in df.columns else 'N/A'}**

📍 Top Location :
**{top_location(df) if 'Location' in df.columns else 'N/A'}**
"""
        )

    with insight2:

        st.info(
            f"""
### 📈 Performance Summary

⭐ Average Rating :
**{average_rating(df) if 'Review Rating' in df.columns else 'N/A'}**

👥 Customers :
**{total_customers(df)}**

💰 Revenue :
**${total_revenue(df):,.2f}**
"""
        )
            # =====================================================
    # ANALYTICS DASHBOARD
    # =====================================================

    st.markdown("---")
    st.subheader("📊 Analytics Dashboard")

    # -------------------- Row 1 --------------------

    col1, col2 = st.columns(2)

    with col1:
        if {"Category", "Purchase Amount (USD)"}.issubset(df.columns):
            st.plotly_chart(
                sales_by_category_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Category chart unavailable.")

    with col2:
        if {"Location", "Purchase Amount (USD)"}.issubset(df.columns):
            st.plotly_chart(
                sales_by_location_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Location chart unavailable.")

    # -------------------- Row 2 --------------------

    col3, col4 = st.columns(2)

    with col3:
        if "Gender" in df.columns:
            st.plotly_chart(
                gender_distribution_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Gender chart unavailable.")

    with col4:
        if "Payment Method" in df.columns:
            st.plotly_chart(
                payment_method_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Payment Method chart unavailable.")

    # -------------------- Row 3 --------------------

    col5, col6 = st.columns(2)

    with col5:
        if {"Season", "Purchase Amount (USD)"}.issubset(df.columns):
            st.plotly_chart(
                season_sales_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Season chart unavailable.")

    with col6:
        if "Review Rating" in df.columns:
            st.plotly_chart(
                rating_distribution_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Rating chart unavailable.")

    # -------------------- Row 4 --------------------

    col7, col8 = st.columns(2)

    with col7:
        if "Item Purchased" in df.columns:
            st.plotly_chart(
                item_purchased_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Item Purchased chart unavailable.")

    with col8:
        if "Age" in df.columns:
            st.plotly_chart(
                age_distribution_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Age chart unavailable.")

    # =====================================================
    # ADDITIONAL ANALYTICS
    # =====================================================

    st.markdown("---")
    st.subheader("📈 Additional Analytics")

    col9, col10 = st.columns(2)

    with col9:
        if "Subscription Status" in df.columns:
            st.plotly_chart(
                subscription_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Subscription chart unavailable.")

    with col10:
        if "Shipping Type" in df.columns:
            st.plotly_chart(
                shipping_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Shipping chart unavailable.")

    col11, col12 = st.columns(2)

    with col11:
        if "Size" in df.columns:
            st.plotly_chart(
                size_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Size chart unavailable.")

    with col12:
        if "Color" in df.columns:
            st.plotly_chart(
                color_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Color chart unavailable.")

    col13, col14 = st.columns(2)

    with col13:
        if "Frequency of Purchases" in df.columns:
            st.plotly_chart(
                frequency_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Frequency chart unavailable.")

    with col14:
        if "Preferred Payment Method" in df.columns:
            st.plotly_chart(
                preferred_payment_chart(df),
                use_container_width=True,
            )
        else:
            st.warning("Preferred Payment chart unavailable.")

    if "Discount Applied" in df.columns:
        st.plotly_chart(
            discount_chart(df),
            use_container_width=True,
        )
    else:
        st.warning("Discount chart unavailable.")

    # =====================================================
    # QUICK SUMMARY
    # =====================================================

    st.markdown("---")
    st.subheader("📈 Quick Business Summary")

    left, right = st.columns(2)

    with left:
        st.success(f"""
### 🏆 Business Highlights

📦 Top Category: **{top_category(df) if 'Category' in df.columns else 'N/A'}**

🛍 Top Product: **{top_product(df) if 'Item Purchased' in df.columns else 'N/A'}**

📍 Best Location: **{top_location(df) if 'Location' in df.columns else 'N/A'}**
""")

    with right:
        st.info(f"""
### 📊 Dashboard Summary

⭐ Average Rating: **{average_rating(df) if 'Review Rating' in df.columns else 'N/A'}**

👥 Customers: **{total_customers(df)}**

💰 Revenue: **${total_revenue(df):,.2f}**
""")
            # =====================================================
    # PROCESSED DATASET
    # =====================================================

    st.markdown("---")
    st.subheader("📋 Processed Dataset")

    st.dataframe(
        df,
        use_container_width=True,
        height=500,
    )

    # =====================================================
    # DATASET INFORMATION
    # =====================================================

    st.markdown("---")
    st.subheader("📊 Dataset Information")

    info1, info2, info3, info4 = st.columns(4)

    with info1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with info2:
        st.metric(
            "Columns",
            df.shape[1]
        )

    with info3:
        st.metric(
            "Missing Values",
            int(df.isnull().sum().sum())
        )

    with info4:
        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )

    # =====================================================
    # DATA PREVIEW
    # =====================================================

    st.markdown("---")
    st.subheader("🔍 First 10 Records")

    st.dataframe(
        df.head(10),
        use_container_width=True
    )

    # =====================================================
    # COLUMN NAMES
    # =====================================================

    with st.expander("📋 View Dataset Columns"):
        st.write(df.columns.tolist())

    # =====================================================
    # DOWNLOAD SECTION
    # =====================================================

    st.markdown("---")
    st.subheader("⬇ Download Processed Dataset")

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name="processed_customer_data.csv",
        mime="text/csv",
    )

    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("---")

    st.markdown(
        """
        <div style="
            background:#F8F9FA;
            padding:20px;
            border-radius:15px;
            text-align:center;
            box-shadow:0px 2px 8px rgba(0,0,0,0.1);
        ">




        <hr>

        <p>
        Customer Shopping Trends Analysis Project
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

else:

    st.info("📂 Please upload your Customer Shopping CSV dataset to begin.")