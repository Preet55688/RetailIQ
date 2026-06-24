import matplotlib.pyplot as plt
import seaborn as sns
from analytics import get_monthly_sales, get_category_sales, get_top_products, get_city_sales, get_sales_data, get_low_stock

def plot_monthly_sales():
    df = get_monthly_sales()
    df["Month"] = df["Month"].astype(str)

    plt.figure(figsize=(8, 5))
    sns.lineplot(data=df, x="Month", y="Revenue", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("images/monthly_sales_trend.png")
    plt.show()

def plot_category_sales():
    df = get_category_sales()

    plt.figure(figsize=(7, 5))
    sns.barplot(data=df, x="Category", y="Revenue", palette="viridis")
    plt.title("Category-wise Sales")
    plt.xlabel("Category")
    plt.ylabel("Revenue (₹)")
    plt.tight_layout()
    plt.savefig("images/category_sales.png")
    plt.show()

def plot_top_products():
    df = get_top_products()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=df, x="Total_Revenue", y="Product_Name", palette="magma")
    plt.title("Top 5 Products by Revenue")
    plt.xlabel("Revenue (₹)")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.savefig("images/top_products.png")
    plt.show()

def plot_city_distribution():
    df = get_city_sales()

    plt.figure(figsize=(7, 7))
    plt.pie(df["Revenue"], labels=df["City"], autopct="%1.1f%%", startangle=90)
    plt.title("Revenue Distribution by City")
    plt.tight_layout()
    plt.savefig("images/city_distribution.png")
    plt.show()

def plot_correlation_heatmap():
    df = get_sales_data()
    numeric_cols = df[["Quantity", "Price", "Stock", "Revenue"]]

    plt.figure(figsize=(6, 5))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("images/correlation_heatmap.png")
    plt.show()

def plot_low_stock():
    df = get_low_stock()

    plt.figure(figsize=(7, 5))
    sns.barplot(data=df, x="Product_Name", y="Stock", color="red")
    plt.axhline(y=10, color="black", linestyle="--", label="Reorder Threshold")
    plt.title("Low Stock Alert")
    plt.xlabel("Product")
    plt.ylabel("Stock")
    plt.legend()
    plt.tight_layout()
    plt.savefig("images/low_stock.png")
    plt.show()

if __name__ == "__main__":
    plot_monthly_sales()
    plot_category_sales()
    plot_top_products()
    plot_city_distribution()
    plot_correlation_heatmap()
    plot_low_stock()