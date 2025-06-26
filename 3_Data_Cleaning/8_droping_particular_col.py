import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)
print(df.isna().sum())
print("*"*100)

# drop a particular rows with missing value in the partcular column

# df.dropna(subset=['Date'],inplace=True,ignore_index=True)
# print(df)
# print(df.isna().sum())

df.dropna(subset=['Calories'],inplace=True,ignore_index=True)
print(df)
print(df.isna().sum())

# df.dropna(subset=['Date','Calories'],inplace=True,ignore_index=True)
# print(df)
# print(df.isna().sum())





