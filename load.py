import pandas as pd 


import sqlite3

def load_data(df, db_name="../data/real_estate.db"):
    print("💾 Loading data...")
    df.to_csv("C:\\Users\\joshi\\Desktop\\python\\Python_Pipelines_Project\\data\\Real_Estate_Sales_2001-2023_GL.csv", index=False)
    print("✅ Data loaded successfully into database!")

