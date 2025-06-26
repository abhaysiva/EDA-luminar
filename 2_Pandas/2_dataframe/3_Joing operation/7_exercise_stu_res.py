import pandas as pd
import numpy as np
df1=pd.read_csv('/Users/Acer/Downloads/student.csv',sep=',')
print(df1)

df2=pd.read_csv('/Users/Acer/Downloads/result.csv',sep=',')
print(df2)
print("*"*100)
df3=pd.merge(df1,df2,on='roll',how='inner').loc[df2['res']=='pass'][['name','res','roll']]
print(df3)

print(df3.index)
# Index([2, 3, 5, 7, 8, 9, 10, 14, 15, 16, 17, 18], dtype='int64')

print("no: of students pass:",len(df3.index))

print("no: of students pass:",df3.shape[0])

