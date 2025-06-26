import pandas as pd
df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)

df1=df.iloc[3]  # PRINT DETAILS OF 3RD ROW
print(df1)
print("*"*100)

#
df1=df.iloc[3:7]   #print from 3rd row to 6th row
print(df1)
print("*"*100)
#
df1=df.iloc[3:30:3]   #print from 3rd row to 29th row with step count 3
print(df1)
print("*"*100)

df1=df.iloc[3:30,1:4]  #print row from 3rd row  to 29th row AND print column from 1st col to 3rd col
print(df1)
print("*"*100)