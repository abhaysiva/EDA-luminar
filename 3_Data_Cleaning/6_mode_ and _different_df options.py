import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)
print(df.isna().sum())
print("*"*100)

# mode ==> most repeated value ==>object

x= df['Date'].mode()[0]
# df['Date'].fillna(x,inplace=True)
#df.fillna({'Date': x}, inplace=True)
df['Date'] = df['Date'].fillna(x)




print('MODE:',x)
print(df)