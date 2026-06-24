from reports import convert_df_to_csv, convert_df_to_excel
import streamlit as st
from analytics import (
    get_kpis, get_monthly_sales, get_category_sales, get_top_products,
    get_low_stock, get_city_sales, get_top_customers
)
from database import fetch_table
from reports import convert_df_to_csv, convert_df_to_excel
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="RetailIQ Dashboard", layout="wide")

st.sidebar.title("RetailIQ 📊")
page = st.sidebar.radio(
    "Navigate",
    ["Dashboard Home", "Sales Dashboard", "Inventory Dashboard", "Customer Dashboard"]
)

if page == "Dashboard Home":
    st.title("📊 RetailIQ Dashboard Home")

    kpis = get_kpis()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"₹{kpis['Total Revenue']:,.0f}")
    col2.metric("Total Orders", kpis['Total Orders'])
    col3.metric("Avg Order Value", f"₹{kpis['Average Order Value']:,.0f}")

elif page == "Sales Dashboard":
    st.title("📈 Sales Dashboard")

    st.subheader("Monthly Sales Trend")
    monthly = get_monthly_sales()
    monthly["Month"] = monthly["Month"].astype(str)
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    sns.lineplot(data=monthly, x="Month", y="Revenue", marker="o", ax=ax1)
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Category-wise Sales")
        category = get_category_sales()
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        sns.barplot(data=category, x="Category", y="Revenue", ax=ax2)
        st.pyplot(fig2)

    with col2:
        st.subheader("Top 5 Products")
        top = get_top_products()
        fig3, ax3 = plt.subplots(figsize=(5, 4))
        sns.barplot(data=top, x="Total_Revenue", y="Product_Name", ax=ax3)
        st.pyplot(fig3)

    st.subheader("⬇️ Download Sales Report")
    dl_col1, dl_col2 = st.columns(2)
    with dl_col1:
        st.download_button(
            "Download Monthly Sales (CSV)",
            data=convert_df_to_csv(monthly),
            file_name="monthly_sales.csv",
            mime="text/csv"
        )
    with dl_col2:
        st.download_button(
            "Download Monthly Sales (Excel)",
            data=convert_df_to_excel(monthly),
            file_name="monthly_sales.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

elif page == "Inventory Dashboard":
    st.title("📦 Inventory Dashboard")

    products_df = fetch_table("Product")

    st.subheader("Current Stock Levels")
    st.dataframe(products_df[["Product_ID", "Product_Name", "Category", "Stock"]])

    st.subheader("⚠️ Low Stock Alerts")
    low_stock = get_low_stock(threshold=10)

    if low_stock.empty:
        st.success("All products have sufficient stock.")
    else:
        st.warning(f"{len(low_stock)} product(s) need reordering!")
        st.dataframe(low_stock)

    st.subheader("⬇️ Download Inventory Report")
    st.download_button(
        "Download Stock Report (CSV)",
        data=convert_df_to_csv(products_df),
        file_name="inventory_report.csv",
        mime="text/csv"
    )

elif page == "Customer Dashboard":
    st.title("🛒 Customer Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales by City")
        city = get_city_sales()
        fig4, ax4 = plt.subplots(figsize=(5, 5))
        plt.pie(city["Revenue"], labels=city["City"], autopct="%1.1f%%", startangle=90)
        st.pyplot(fig4)

    with col2:
        st.subheader("Top 5 Customers")
        top_cust = get_top_customers()
        st.dataframe(top_cust)

    st.subheader("⬇️ Download Customer Report")
    st.download_button(
        "Download Top Customers (CSV)",
        data=convert_df_to_csv(top_cust),
        file_name="top_customers.csv",
        mime="text/csv"
    )