# fillna()

# fillna() ===>  overall filling

import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)

# print(df.isna().sum())
# df.fillna(300,inplace=True) # it Replace every NaN with onr particular value
#
# print(df.isna().sum())
# print(df)

df['Calories'].fillna(300,inplace=True)
print(df)
print(df.isna().sum())

