import matplotlib.pyplot as plt

def visualize_data(df):
    print("Creating visualization")

    avg_sales=df.groupby('Sale Year')['Sale Amount'].mean()
    avg_sales.plot(kind='line', title='Average Sale Amount by year')

    plt.xlabel('Year')
    plt.ylabel('Average Sale Amount')
    plt.grid(True)
    plt.savefig("C:\\Users\\joshi\\Desktop\\python\\Python_Pipelines_Project\\Images")
    plt.show()  
    print("Visualization saved successfully!")
    
