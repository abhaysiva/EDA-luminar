import numpy as np
import pandas as pd

dic={"id":[1,2,3,4,5],"Fname":["Abhay","Vandana","Hitha","Nithin","Belvin"],"Lname":["A","M","S","F","D"],"Age":[23,24,20,20,24]}

df=pd.DataFrame(dic)
print(df)

print("*"*100)

print(df.describe())

print(df.describe(include="O"))

