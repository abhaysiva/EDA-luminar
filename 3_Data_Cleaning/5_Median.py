import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)
print(df.isna().sum())
print("*"*100)

# Median ==> middle value ==> used for integers ( numerical data) ==>ascending order


x =df ['Calories'].median()
df['Calories'].fillna(x,inplace=True)
print("Median:",x)
print(df)




