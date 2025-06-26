import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/customer5.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location','salary']
print(df)

print(df.isna().sum())
print("*"*100)


#1. Each profession count  [count desc]
df1=df.groupby('prof')['prof'].count()\
    .sort_values()
print(df1)
print("*"*100)


#2. Each profession maximum salary  [salary desc]
df1=df.groupby('prof')['salary'].max()\
    .sort_values(ascending=False)
print(df1)
print("*"*100)


#3. Each location min salary  [salary asc]
df1=df.groupby('location')['salary'].min()\
    .sort_values(ascending=True)
print(df1)
print("*"*100)


#4. Each profession total salary
df1=df.groupby('prof')['salary'].sum()\
    .sort_values(ascending=True)
print(df1)
print("*"*100)


#5. Each location average age
df1=df.groupby('location')['age'].mean()\
    .sort_values(ascending=True)
print(df1)
print("*"*100)


#6. Each profession maximum age
df1=df.groupby('prof')['age'].max()\
    .sort_values(ascending=True)
print(df1)
print("*"*100)
