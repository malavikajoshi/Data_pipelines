import pandas as pd 
# from extract import extract_data

def extract_data(file_path):
    print("Extracting data.....")
    df=pd.read_csv("C:\\Users\\joshi\\Desktop\\python\\Python_Pipelines_Project\\data\\Real_Estate_Sales_2001-2023_GL.csv", low_memory=False)
    print(f" Data Extracted successfully! shape:{df.shape}")
    return df

df=extract_data("C:\\Users\\joshi\\Desktop\\python\\Python_Pipelines_Project\\data\\Real_Estate_Sales_2001-2023_GL.csv")
df.head()