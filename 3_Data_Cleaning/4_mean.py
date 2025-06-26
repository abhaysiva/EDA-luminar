import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)
print(df.isna().sum())
print("*"*100)


# Mean  ==> used for float( numerical data)

x=df['Calories'].mean()
df['Calories'].fillna(x,inplace=True)

print("MEAN:",x)
print(df)




