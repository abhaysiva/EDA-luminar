import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)
print(df.isna().sum())


df['Calories'].fillna(300,inplace=True)
print(df)
print(df.isna().sum())

df['Date'].fillna('2020/12/12',inplace=True)
print(df)
print(df.isna().sum())