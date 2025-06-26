# 1. name ,age ,dalarya ,dat ,amount
# 2.Age above 26name ,age , salary ,dat
# age minimum 1 emp name ,age ,location ,dat ,amount
# Latest date ,name ,age ,slaaray ,dat ,amount

import pandas as pd


df1=pd.read_csv('/Users/Acer/Downloads/custom_windows.csv',sep=',')
print(df1)
print("*"*100)
df2=pd.read_csv('/Users/Acer/Downloads/order_windows.csv',sep=',')
print(df2)
print("*"*100)
df3=pd.merge(df1,df2,on='id',how='inner')
print(df3)
print("*"*100)

   # id      name  age location  salary  oid                  dat  amount
# 0   2    Rachel   25    Delhi    1500  101  2016-11-20 00:00:00    1560
# 1   3  Chandler   23     Kota    2000  102  2016-10-08 00:00:00    3000
# 2   3  Chandler   23     Kota    2000  100  2016-10-08 00:00:00    1500
# 3   4    Monika   25   Mumbai    6500  103  2015-05-20 00:00:00    2060


# 1. name ,age ,dalarya ,dat ,amount

df4=df3[['name','age','salary','dat','amount']]
print(df4)
print("*"*100)
       # name  age  salary                  dat  amount
# 0    Rachel   25    1500  2016-11-20 00:00:00    1560
# 1  Chandler   23    2000  2016-10-08 00:00:00    3000
# 2  Chandler   23    2000  2016-10-08 00:00:00    1500
# 3    Monika   25    6500  2015-05-20 00:00:00    2060

# 2.Age above 26name ,age , salary ,dat
df4=df3.loc[df3['age']>26][['name','age','salary','dat']]
print(df4)
print("*"*100)
# empty data
# Empty DataFrame
# Columns: [name, age, salary, dat]
# Index: []
# 3.age minimum 1 emp name ,age ,location ,dat ,amount

df4=df3.sort_values(by='age')[['name','age','location','dat','amount']].head(1)
print(df4)
print("*"*100)
       # name  age location                  dat  amount
# 1  Chandler   23     Kota  2016-10-08 00:00:00    3000

# 4.Latest date ,name ,age ,slaaray ,dat ,amount
df4=df3.sort_values(by='dat',ascending=False).head(1)
print(df4)
print("*"*100)
   # id    name  age location  salary  oid                  dat  amount
# 0   2  Rachel   25    Delhi    1500  101  2016-11-20 00:00:00    1560


