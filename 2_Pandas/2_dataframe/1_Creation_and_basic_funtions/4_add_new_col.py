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

df["Gender"]=["M","F","M","F","M","M","M"]
print(df)

print("*"*100)
dic={"id":[1,2,3,4,5],"Fname":["Abhay","Vandana","Hitha","Nithin","Belvin"],"Lname":["A","M","S","F","D"],"Age":[23,24,20,20,24]}

df=pd.DataFrame(dic)

df["Gender"]=['M','F','F','M','M']
print(df)

