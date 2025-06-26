import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)

#sum funtion
df1=df.groupby('prof')['age'].sum()\
    .sort_values(ascending=True)
print(df1)
print("*"*100)

# africa 58 ,due to missing value
