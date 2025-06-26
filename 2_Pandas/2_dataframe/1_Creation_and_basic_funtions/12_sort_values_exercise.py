import pandas as pd
import numpy as np


df2=pd.read_csv('/Users/Acer/Downloads/sample4.txt',sep=',',header=None)
df2.columns=['id','fname','lname','age','phno','location']
print(df2)
print("*"*100)

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

df3= df2.loc[df2['location']=='Chennai'].sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'phno']].head(1)
print(df3)
print("*"*100)