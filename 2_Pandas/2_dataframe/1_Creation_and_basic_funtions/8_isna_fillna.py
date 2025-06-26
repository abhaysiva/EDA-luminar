import pandas as pd
df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)


print(df.columns) # to print name of cols
# Index(['id', 'fname', 'lname', 'age', 'prof', 'location'], dtype='object')
print("*"*100)

print(df.isna().sum())
# id          0
# fname       0
# lname       0
# age         0
# prof        0
# location    1
# dtype: int64
print("*"*100)

# fillna()
# using for filling value commanly using one particular value

df1=df.fillna('india')
print(df1.isna().sum())
# id          0
# fname       0
# lname       0
# age         0
# prof        0
# location    0
# dtype: int64
print("*"*100)