# 📊 Data Pipelines Project

This project demonstrates how to build and analyze a **data pipeline** to process and visualize sales data over multiple years. It focuses on understanding sales performance by computing the **Average Sale Amount by Year** and generating clear visual insights using Python.

## 🧩 Project Objective

The main objective of this project is to create a simple, automated data pipeline that:
1. **Extracts** raw sales data.
2. **Transforms** the data through cleaning and aggregation.
3. **Loads** the processed data for analysis and visualization.
4. **Visualizes** the results to identify sales trends over time.

This approach follows the standard **ETL (Extract, Transform, Load)** process commonly used in data engineering and analytics.

## 📈 Visualization Overview

The final output of the pipeline is a line graph showing the **Average Sale Amount by Year**.

<img width="640" height="480" alt="Images" src="https://github.com/user-attachments/assets/8a9b9bbd-59bd-45d1-8735-91a114f71de6" />

**Figure:** The graph shows how the average sales amount has changed from the year 2000 to 2025.  
You can observe a general upward trend, with fluctuations that may represent market variations or seasonal factors.

## ⚙️ Workflow Steps

**1. Data Extraction**
- Load the dataset using **Pandas** from a CSV file or a database.
- Example:
  ```python
  import pandas as pd
  df = pd.read_csv('sales_data.csv')

**2. Data Cleaning**
Handle missing or duplicate entries.
Convert date columns into proper datetime format.
Ensure that all numeric columns (like sales amounts) are in consistent units.

**3. Data Transformation**
Group data by Year and calculate the average sale amount:
avg_sales = df.groupby('Year')['SaleAmount'].mean()

**4. Data Visualization**
Use Matplotlib to visualize the yearly average sales:
import matplotlib.pyplot as plt

plt.plot(avg_sales.index, avg_sales.values)
plt.title("Average Sale Amount by Year")
plt.xlabel("Year")
plt.ylabel("Average Sale Amount")
plt.show()

This plot helps in understanding long-term sales performance and identifying growth patterns.

**🧠 Key Learnings**
Through this project, you will:
-->Understand the ETL process (Extract, Transform, Load).
-->Gain hands-on experience with Pandas for data manipulation.
-->Learn how to create clear and meaningful visualizations using Matplotlib.
-->Develop an understanding of how to interpret time-series data trends.

| Category             | Tools/Libraries            |
| -------------------- | -------------------------- |
| Programming Language | Python                     |
| Data Handling        | Pandas, NumPy              |
| Visualization        | Matplotlib                 |
| Environment          | Jupyter Notebook / VS Code |

**📂 Project Structure**
Data_pipelines/
│
├── data/                 # Contains raw and cleaned data files
├── notebooks/            # Jupyter notebooks for step-by-step analysis
├── scripts/              # Python scripts for automation
├── visuals/              # Generated graphs and charts
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

**🧾 How to Run the Project**
1.Clone the Repository
-----------------------------------
git clone https://github.com/malavikajoshi/Data_pipelines.git
cd Data_pipelines

2.Install Required Packages
-----------------------------------
pip install -r requirements.txt

3.Run the Notebook or Script
----------------------------------
For Jupyter Notebook:
jupyter notebook notebooks/data_pipeline.ipynb

Or directly execute the script:
python scripts/data_pipeline.py

4.View the Visualization
----------------------------------
The generated plot will display the yearly average sales trend.
It will also be saved inside the visuals/ folder.

**🔮 Future Improvements**
Automate the pipeline using Apache Airflow or Prefect.
Connect to a live SQL database for real-time data updates.
Build an interactive dashboard using Streamlit or Power BI.
Incorporate additional metrics such as total revenue or region-wise performance.
