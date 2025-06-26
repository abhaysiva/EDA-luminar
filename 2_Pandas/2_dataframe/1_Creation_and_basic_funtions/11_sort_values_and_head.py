#sort_values
# it is use for the sorting process based on a col

import pandas as pd
import numpy as np


df1=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df1.columns=['id','fname','lname','age','prof','location']
print(df1)

print("*"*100)

df=df1.sort_values(by='age')
print(df1)
# index will remain as the first data sets index

print("*"*100)
df1=df.sort_values(by='age',ascending=False)
print(df1)


# priority order
# loc sort column row

df2=pd.read_csv('/Users/Acer/Downloads/sample4.txt',sep=',',header=None)
df2.columns=['id','fname','lname','age','phno','location']
print(df2)

#1. Age mxm 2 empl fname , lname ,age ,phno
df3 = df2.sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'phno','location']].head(2)
print(df3)
print("*"*100)
#2. age minimum 1 emp fname , lname ,age

df3 = df2.sort_values(by='age')\
    [['fname', 'lname', 'age']].head(1)
print(df3)
print("*"*100)
#3.chenni work ,age max 1 emp fname ,lname ,agee ,phno

df3= df2.loc[df2['location']=='chennai'].sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'phno']].head(1)
print(df1)
print("*"*100)