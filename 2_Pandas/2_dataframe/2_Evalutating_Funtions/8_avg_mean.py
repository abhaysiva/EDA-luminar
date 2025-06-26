import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)

# avg == mean()
df1=df.groupby('prof')['age'].mean()\
    .sort_values(ascending=True)
print(df1)
print("*"*100)



