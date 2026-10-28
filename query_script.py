import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///retail_database.db')

print("=== 1. Top 5 Best-Selling Products by Total Revenue ===")
query1 = """
    SELECT Description, SUM(TotalPrice) as Revenue 
    FROM fact_sales 
    GROUP BY Description 
    ORDER BY Revenue DESC 
    LIMIT 5
"""
df_top_products = pd.read_sql(query1, engine)
print(df_top_products)#tnadhf w tmed cleaned top 5

print("\n=== 2. Total Sales Revenue by Country ===")
query2 = """
    SELECT Country, SUM(TotalPrice) as TotalSales 
    FROM fact_sales 
    GROUP BY Country 
    ORDER BY TotalSales DESC 
    LIMIT 5
"""
df_countries = pd.read_sql(query2, engine)
print(df_countries)