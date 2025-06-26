#filter  ==> loc


import numpy as np
import pandas as pd

df=pd.read_csv('/Users/Acer/Downloads/sample4.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','phno','location']
print(df)
print("*"*100)

# loc condition

#newdfname =oldfname.loc[df['colname']condition]


# collect only the data of age above 22
df1=df.loc[df['age']>22]
print(df1)
print("*"*100)

# age equal to 21 fname,lname ,age ,phno
df1=df.loc[df['age']==21] [['fname','lname','age','phno']]
print(df1)
print("*"*100)


#age equal to 23 fname ,lname ,age
df1=df.loc[df['age']==23] [['fname','lname','age']]
print(df1)
print("*"*100)

#chennai work fname,lname,age ,phone
df1=df.loc[df['location']=='Chennai'] [['fname','lname','age','phno']]
print(df1)
print("*"*100)

#age above 23 and loc chennai fname ,lname, age
df1=df.loc[(df['age']>23) & (df['location']=='Chennai')] [['fname','lname','age']]
print(df1)
print("*"*100)







