import pandas as pd

def transform_data(df):
    print("Transforming data.....")
    df=df.dropna(subset=['Sale Amount'])
    df=df[df['Sale Amount']>0]
    df['Date Recorded']=pd.to_datetime(df['Date Recorded'], errors='coerce')
    df = df.drop_duplicates()
    df['Sale Year'] = df['Date Recorded'].dt.year

    print(f"Data transformed successfully! shape:{df.shape}")
    return df


# ✅ Concepts learned here:
# dropna() → removes missing values
# to_datetime() → converts text to date
# drop_duplicates() → removes repeated rows
# df['column'].dt.year → extracts year from date