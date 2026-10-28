# Online Retail ETL Pipeline & SQL Analysis

An end-to-end Data Engineering project that extracts raw e-commerce transaction data, performs automated data cleaning and transformation using Python (Pandas), loads structured data into a relational database (SQLite), and executes SQL queries for business insights.

## 🛠️ Tech Stack & Tools
- **Language:** Python
- **Libraries:** Pandas, SQLAlchemy
- **Database:** SQLite
- **Data Source:** UCI Online Retail Dataset (~540k records)

## 🔄 ETL Pipeline Overview
1. **Extract:** Loads raw CSV transaction records.
2. **Clean:** Removes null customer IDs, negative quantities, and price anomalies (~541k raw rows filtered down to ~397k clean records).
3. **Transform:** Performs feature engineering, including calculating total revenue (`TotalPrice = Quantity * UnitPrice`).
4. **Load:** Automatically builds and loads the structured data into SQLite (`fact_sales` table).

## 📊 Business Insights (SQL)
Using SQL queries executed via `query_script.py`, key metrics were extracted:
- **Top Product by Revenue:** *Paper Craft, Little Birdie* ($168,469.60)
- **Top International Markets:** United Kingdom, Netherlands, EIRE, Germany, and France.

## 🚀 How to Run
```bash
# 1. Run the ETL Pipeline
python etl_script.py

# 2. Run the SQL Analysis Queries
python query_script.py# online-retail-etl
An end-to-end Python ETL pipeline and SQL analysis on online retail data.
