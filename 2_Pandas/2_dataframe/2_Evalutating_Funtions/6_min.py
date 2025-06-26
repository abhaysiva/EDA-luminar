import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)

# min function
df1=df.groupby('prof')['age'].min()\
    .sort_values()
print(df1)
print("*"*100)