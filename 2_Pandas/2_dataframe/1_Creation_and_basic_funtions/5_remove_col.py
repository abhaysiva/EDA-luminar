import numpy as np
import pandas as pd

lst=[[1,"Abhay","Siva",23,"Python",10000],
   [2,"Suma","Siva",50,"Bigdata",15550],
   [3,"Athul","Suresh",29,"Bigdata",20000],
   [4,"Rashitha","Remesh",30,"SQL",25000],
   [5,"Sivan","P",65,"Flutter",10000],
   [6,"Jyothish","Parthip",23,"Flutter",25000],
   [7,"Yadhu","Chandra",23,"Python",15000]]
df=pd.DataFrame(lst)
df.columns=['id','fname','lname','age','prof','salary']
print(df)


print("*"*100)

# how to remove a column
df1=df.drop(['prof'],axis=1)  # axis is for defineing the col
print(df1)

   # id     fname    lname  age  salary
# 0   1     Abhay     Siva   23   10000
# 1   2      Suma     Siva   50   15550
# 2   3     Athul   Suresh   29   20000
# 3   4  Rashitha   Remesh   30   25000
# 4   5     Sivan        P   65   10000
# 5   6  Jyothish  Parthip   23   25000
# 6   7     Yadhu  Chandra   23   15000

# how to remove multiole column

df1=df.drop(['prof','salary'],axis=1)
print(df1)

   # id     fname    lname  age
# 0   1     Abhay     Siva   23
# 1   2      Suma     Siva   50
# 2   3     Athul   Suresh   29
# 3   4  Rashitha   Remesh   30
# 4   5     Sivan        P   65
# 5   6  Jyothish  Parthip   23
# 6   7     Yadhu  Chandra   23