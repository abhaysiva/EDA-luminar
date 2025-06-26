import numpy as np
import  pandas as pd

lst=[[1,"Abhay","Siva",23,"Python",10000],
   [2,"Suma","Siva",50,"Bigdata",15550],
   [3,"Athul","Suresh",29,"Bigdata",20000],
   [4,"Rakesh","Remesh",30,"SQL",25000],
   [5,"Sivan","P",65,"Flutter",10000],
   [6,"Jyothish","Parthip",23,"Flutter",25000],
   [7,"Yadhu","Chandra",23,"Python",15000]]
print(lst)
# [[1, 'Abhay', 'Siva', 23, 'Bigdata', 10000], [2, 'Suma', 'Sivan', 50, 'Python', 15550], [3, 'Athul', 'Suresh', 29, 'Bigdata', 20000], [4, 'Rakesh', 'Remesh', 30, 'SQL', 2500], [5, 'Sivan', 'P', 65, 'Flutter', 10000], [6, 'Jyothish', 'Parthip', 23, 'Flutter', 25000], [7, 'Yadhu', 'Chandra', 23, 'Python', 15000]]


df=pd.DataFrame(lst)
print(df)

   # 0         1        2   3        4      5
# 0  1     Abhay     Siva  23  Bigdata  10000
# 1  2      Suma    Sivan  50   Python  15550
# 2  3     Athul   Suresh  29  Bigdata  20000
# 3  4    Rakesh   Remesh  30      SQL   2500
# 4  5     Sivan        P  65  Flutter  10000
# 5  6  Jyothish  Parthip  23  Flutter  25000
# 6  7     Yadhu  Chandra  23   Python  15000
print('*'*100)

df.columns=['id','fname','lname','age','prof','salary']
print(df)
   # id     fname    lname  age     prof  salary
# 0   1     Abhay     Siva   23  Bigdata   10000
# 1   2      Suma    Sivan   50   Python   15550
# 2   3     Athul   Suresh   29  Bigdata   20000
# 3   4    Rakesh   Remesh   30      SQL    2500
# 4   5     Sivan        P   65  Flutter   10000
# 5   6  Jyothish  Parthip   23  Flutter   25000
# 6   7     Yadhu  Chandra   23   Python   15000


print(df.shape)#(7, 6)
print(df.size)#42
print(df.ndim)#2

print(df.head(3)) # print first 3 rows
print(df.tail(1)) # print last 1 rows

print(df.dtypes)
# id         int64
# fname     object
# lname     object
# age        int64
# prof      object
# salary     int64
# dtype: object


