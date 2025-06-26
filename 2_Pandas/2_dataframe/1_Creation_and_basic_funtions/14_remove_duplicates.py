#how to remove duplicate values
# drop_duplicates()  ===>msq=distinct
import numpy as np
import pandas as pd

df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)

df3=df.drop_duplicates()
print(df3)
print("*"*100)


