import numpy as np
import pandas as pd

lst=[[1,"Abhay","Siva",23,"Python",10000],
   [2,"Suma","Siva",50,"Bigdata",15550],
   [3,"Athul","Suresh",29,"Bigdata",20000],
   [4,"Rakesh","Remesh",30,"SQL",25000],
   [5,"Sivan","P",65,"Flutter",10000],
   [6,"Jyothish","Parthip",23,"Flutter",25000],
   [7,"Yadhu","Chandra",23,"Python",15000]]
df=pd.DataFrame(lst)
df.columns=['id','fname','lname','age','prof','salary']
print(df)



print("*"*100)

print(df.describe())
             # id        age        salary
# count  7.000000   7.000000      7.000000
# mean   4.000000  34.714286  14007.142857
# std    2.160247  16.418631   7355.860961
# min    1.000000  23.000000   2500.000000
# 25%    2.500000  23.000000  10000.000000
# 50%    4.000000  29.000000  15000.000000
# 75%    5.500000  40.000000  17775.000000
# max    7.000000  65.000000  25000.000000

print(df.describe(include="O"))
        # fname lname     prof
# count       7     7        7
# unique      7     6        4   #count without repeatation
# top     Abhay  Siva   Python   #most repeated values in eachh col
# freq        1     2        2   #how many times the top values repeated

print(df.describe(include="all"))
              # id  fname lname        age    prof        salary
# count   7.000000      7     7   7.000000       7      7.000000
# unique       NaN      7     6        NaN       4           NaN
# top          NaN  Abhay  Siva        NaN  Python           NaN
# freq         NaN      1     2        NaN       2           NaN
# mean    4.000000    NaN   NaN  34.714286     NaN  17221.428571
# std     2.160247    NaN   NaN  16.418631     NaN   6334.551888
# min     1.000000    NaN   NaN  23.000000     NaN  10000.000000
# 25%     2.500000    NaN   NaN  23.000000     NaN  12500.000000
# 50%     4.000000    NaN   NaN  29.000000     NaN  15550.000000
# 75%     5.500000    NaN   NaN  40.000000     NaN  22500.000000
# max     7.000000    NaN   NaN  65.000000     NaN  25000.000000




print("*"*100)
dic={"id":[1,2,3,4,5],"Fname":["Abhay","Vandana","Hitha","Nithin","Belvin"],"Lname":["A","M","S","F","D"],"Age":[23,24,20,20,24]}

df=pd.DataFrame(dic)
print(df)

print(df.describe(include="all"))