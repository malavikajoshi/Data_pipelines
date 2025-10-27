from extract import extract_data
from transform import transform_data
from load import load_data
from visualize import visualize_data

def main():
    file_path="C:\\Users\\joshi\\Desktop\\python\\Python_Pipelines_Project\\data\\Real_Estate_Sales_2001-2023_GL.csv"
    # satge 1: Extract
    df=extract_data(file_path)

    # stage 2: Transform
    df=transform_data(df)

    # stage 3:load
    load_data(df)

    # stage 4:visualize
    visualize_data(df)

if __name__=="__main__":
    main()