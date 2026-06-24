import pandas as pd
from database import fetch_table

def get_sales_data():
    orders = fetch_table("Orders")
    products = fetch_table("Product")
    merged = orders.merge(products, on="Product_ID", how="left")
    merged["Revenue"] = merged["Quantity"] * merged["Price"]
    return merged

def get_monthly_sales():
    df = get_sales_data()
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    df["Month"] = df["Order_Date"].dt.to_period("M")
    monthly_sales = df.groupby("Month")["Revenue"].sum().reset_index()
    return monthly_sales

def get_category_sales():
    df = get_sales_data()
    category_sales = df.groupby("Category")["Revenue"].sum().reset_index()
    category_sales = category_sales.sort_values(by="Revenue", ascending=False)
    return category_sales

def get_top_products(n=5):
    df = get_sales_data()
    product_sales = df.groupby("Product_Name").agg(
        Total_Quantity=("Quantity", "sum"),
        Total_Revenue=("Revenue", "sum")
    ).reset_index()
    product_sales = product_sales.sort_values(by="Total_Revenue", ascending=False)
    return product_sales.head(n)

def get_low_stock(threshold=10):
    products = fetch_table("Product")
    low_stock = products[products["Stock"] < threshold]
    return low_stock[["Product_ID", "Product_Name", "Stock"]]

def get_city_sales():
    df = get_sales_data()
    customers = fetch_table("Customer")
    df = df.merge(customers, on="Customer_ID", how="left")
    city_sales = df.groupby("City")["Revenue"].sum().reset_index()
    city_sales = city_sales.sort_values(by="Revenue", ascending=False)
    return city_sales

def get_top_customers(n=5):
    df = get_sales_data()
    customers = fetch_table("Customer")
    df = df.merge(customers, on="Customer_ID", how="left")
    customer_sales = df.groupby("Name")["Revenue"].sum().reset_index()
    customer_sales = customer_sales.sort_values(by="Revenue", ascending=False)
    return customer_sales.head(n)

def get_kpis():
    df = get_sales_data()

    total_revenue = df["Revenue"].sum()
    total_orders = df["Order_ID"].nunique()
    avg_order_value = total_revenue / total_orders

    kpis = {
        "Total Revenue": total_revenue,
        "Total Orders": total_orders,
        "Average Order Value": round(avg_order_value, 2)
    }
    return kpis

if __name__ == "__main__":
    df = get_sales_data()
    print(df.head())
    print("\nTotal Revenue:", df["Revenue"].sum())

    monthly = get_monthly_sales()
    print("\nMonthly Sales:\n", monthly)

    category = get_category_sales()
    print("\nCategory-wise Sales:\n", category) 

    top_products = get_top_products()
    print("\nTop Products:\n", top_products)

    low_stock = get_low_stock()
    print("\nLow Stock Alerts:\n", low_stock)

    city = get_city_sales()
    print("\nCity-wise Sales:\n", city)

    top_customers = get_top_customers()
    print("\nTop Customers:\n", top_customers)

    kpis = get_kpis()
    print("\nBusiness KPIs:\n", kpis)