import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/txn_windows.csv',sep=',')
print(df)
print(df.isna().sum())
print("*"*100)


# 1.Find Row count
print(df.shape[0])  # Number of rows
print("*"*100)

# print(len(df))  # Number of rows
# len(df) directly counts the number of rows.


# print(df.count())  # Count of non-null values in each column
# print(df.count().max())  # Maximum count of non-null values (total row count if no missing values)






#2.jan month oid,cusno,category,product,state
# A. Row count



# df1=df.loc[(df["dat"]>='01-01-2011') & (df["dat"]<='01-31-2011')]

df['dat'] = pd.to_datetime(df['dat'], format='%m-%d-%Y')  # Convert to datetime
df1 = df[df['dat'].between('2011-01-01', '2011-01-31')][['oid','cuid','category','product','state']]

# we can also use both methods to conditioning in the dates


print(df1)  # Should return rows if dates are correctly converted

print("No: of rows",df1.shape[0])
print("*"*100)


#3.July Month oid,cusno,category,product,state
# B. Row count
df1 = df[df['dat'].between('2011-07-01', '2011-07-31')][['oid','cuid','category','product','state']]
print(df1)

print(df1.shape[0])
print("*"*100)


# 4.Each category [count desc sort]

df1=df.groupby('category')['category'].count()\
    .sort_values(ascending=False)
print(df1)
print("*"*100)

#5.Category full deatils .of the top category
df1=df.loc[df['category']=='Outdoor Recreation']
print(df1)
print("*"*100)



#6.Each paymethod count

df1=df.groupby('method')['method'].count()
print(df1)
print("*"*100)


# 7.jan-july month purchase count [include]

df1=df[df['dat'].between('2011-01-01', '2011-07-31')]
print(df1.shape[0])
print("*"*100)



# 8.Each category total amount
df1= df.groupby('category')['pay_amount'].sum()
print(df1)
print("*"*100)



# 9.Each category maximum amount
df1= df.groupby('category')['pay_amount'].max()
print(df1)
print("*"*100)


# 10.Each category avg amount
df1= df.groupby('category')['pay_amount'].mean()
print(df1)
print("*"*100)




# 11.total amount by cash and credit card
df1=df.groupby('method')['pay_amount'].sum()
print(df1)
print("*"*100)


# 12.Indoor games ,total amount

df1=df.loc[(df['category']=='Indoor Games')].groupby('category')['pay_amount'].sum()
print(df1)




# 13.Each state count
df1=df.groupby('state')['state'].count()
print(df1)





