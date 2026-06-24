# 📊 RetailIQ — Smart Sales & Inventory Analytics Platform

A full-stack data analytics project for retail businesses — tracks sales performance, monitors inventory, analyzes customer behavior, and generates real-time dashboards.

## 🎯 Problem It Solves
Small and medium retail stores often lack a centralized way to track sales, spot low stock, or understand customer buying patterns. RetailIQ solves this with an end-to-end analytics pipeline.

## 🏗️ Tech Stack
- **Database:** MySQL
- **Backend/Analytics:** Python, Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Web Dashboard:** Streamlit
- **Business Intelligence:** Power BI

## 🔑 Features
- Live KPI dashboard (Total Revenue, Orders, Average Order Value)
- Monthly sales trend, category-wise sales, top-selling products
- Automated low-stock alerts (reorder threshold)
- Customer & city-wise revenue analysis
- CSV/Excel report downloads
- 4-page Power BI executive dashboard with DAX measures

## 📂 Project Structure
RetailIQ/

├── app.py              # Streamlit dashboard (4 pages)

├── database.py         # MySQL connection (SQLAlchemy)

├── analytics.py         # Pandas-based analytics functions

├── visualizations.py    # Matplotlib/Seaborn charts

├── reports.py           # CSV/Excel export

├── images/               # Generated charts

├── dashboards/           # Power BI .pbix file

└── requirements.txt

## 🚀 How to Run# RetailIQ — Smart Sales & Inventory Analytics Platform

A full-stack data analytics project for retail businesses — tracks sales performance, monitors inventory, analyzes customer behavior, and generates real-time dashboards.

## Problem It Solves
Small and medium retail stores often lack a centralized way to track sales, spot low stock, or understand customer buying patterns. RetailIQ solves this with an end-to-end analytics pipeline.

## Tech Stack
- Database: MySQL
- Backend/Analytics: Python, Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Web Dashboard: Streamlit
- Business Intelligence: Power BI

## Features
- Live KPI dashboard (Total Revenue, Orders, Average Order Value)
- Monthly sales trend, category-wise sales, top-selling products
- Automated low-stock alerts (reorder threshold)
- Customer and city-wise revenue analysis
- CSV/Excel report downloads
- 4-page Power BI executive dashboard with DAX measures

## Project Structure
- app.py - Streamlit dashboard (4 pages)
- database.py - MySQL connection (SQLAlchemy)
- analytics.py - Pandas-based analytics functions
- visualizations.py - Matplotlib/Seaborn charts
- reports.py - CSV/Excel export
- images/ - Generated charts
- dashboards/ - Power BI .pbix file
- requirements.txt

## How to Run
1. Clone this repo
2. Create a virtual environment and install dependencies: pip install -r requirements.txt
3. Set up a MySQL database named retailiq
4. Create a .env file with your MySQL credentials (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
5. Run the dashboard: streamlit run app.py

## Sample Insights
- Electronics drives ~95% of total revenue
- Bangalore is the top revenue-generating city
- Automated alerts flag products below reorder threshold

## Author
Built as a data analytics portfolio project — demonstrates database design, Python data analysis, dashboard development, and BI reporting.
1. Clone this repo
2. Create a virtual environment and install dependencies:
pip install -r requirements.txt
3. Set up a MySQL database named `retailiq` (schema in `/sql` if included)
4. Create a `.env` file with your MySQL credentials:
DB_HOST=localhost

DB_USER=root

DB_PASSWORD=your_password

DB_NAME=retailiq
5. Run the dashboard:
streamlit run app.py

## 📈 Sample Insights
- Electronics drives ~95% of total revenue
- Bangalore is the top revenue-generating city
- Automated alerts flag products below reorder threshold

## 👤 Author
Built as a data analytics portfolio project — demonstrates database design, Python data analysis, dashboard development, and BI reporting.
Save the file (Ctrl+S).
Now push this new file to GitHub:
git add .
git commit -m "Add README"
git push
Paste me the output of the push.
