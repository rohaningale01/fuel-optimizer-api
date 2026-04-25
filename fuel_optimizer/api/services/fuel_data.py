import pandas as pd

df = pd.read_csv("fuel-prices-for-be-assessment.csv")

def get_all_data():
    return df

def get_cheapest_station():
    return df.loc[df['Retail Price'].idxmin()]