#dropna()

import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)
print(df.isna().sum())
print("*"*100)

# dropna()  ===> droppin of the entire rows,which have missing value

df.dropna(inplace=True,ignore_index=True)  # ignore_index= True   ==> To correct the index
print(df)
print(df.isna().sum())


