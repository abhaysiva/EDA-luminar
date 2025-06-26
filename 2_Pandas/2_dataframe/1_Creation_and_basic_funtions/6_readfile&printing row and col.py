# exxternal file into data frame

import numpy as np
import pandas as pd

df=pd.read_csv('/Users/Acer/Downloads/sample4.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','phno','location']
print(df)
# if we dont mention header tag for a data file with no header file  ,then first row will turned into heared
df1=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df1.columns=['id','fname','lname','age','prof','location']
print(df1)



df2=pd.read_csv('/Users/Acer/Downloads/customer5.txt',sep=',',header=None)
df2.columns=['id','fname','lname','age','prof','location','salary']
print(df2)

df3=pd.read_csv('/Users/Acer/Downloads/movies_cleaned_pandas.csv',sep=',',header=None)
df3.columns=['S.No','Name','Year','Ratings','Runtime']
print(df3)



# print only specific column
df4=df[['fname','lname','age']]
print(df4)



# print first 20 rows with specific column

df5=df1[['fname','lname','age','prof']].head(20)
print(df5)