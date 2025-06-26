import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/heart.csv')
print(df)




# 1) Find total Row of data
print("No: of rows:",df.shape[0])
print("*"*100)

# 2) Find count of target columns
df2=df.loc[df['target']==0]
print("NO: of target '0':",df2.shape[0])
df2=df.loc[df['target']==1]
print("NO: of target '1':",df2.shape[0])
print("*"*100)


#sirmethod
print("sirmethod")
df2=df.groupby('target')['target'].count()\
    .sort_values(ascending=False)
print(df2)


# 3) Age above 75 data's
df3=df.loc[df['age']>75]
print("Age above 75:",df3.shape[0])
print("*"*100)


# 4) Age below 45, Each target count
df4=df.loc[(df['age']<45) & (df['target']==0)]
print("Age above 45 and target =0:",df4.shape[0])
df4=df.loc[(df['age']<45) & (df['target']==1)]
print("Age above 45 and target =1:",df4.shape[0])
print("*"*100)

# sirmethod
print("sirmethod q4")
df4=df.loc[df['target']<45]\
    .groupby('target')['target'].count()\
    .sort_values(ascending=False)
print(df2)

# 5) Age mxm 3 dats's
df5=df.sort_values(by='age',ascending=False).head(3)
print(df5)
print("*"*100)

# 6) Seperate x and y
x=df.iloc[:,:-1]
print(x)
print("*"*100)
y=df.iloc[:,-1:-2:-1]
print(y)
print("*"*100)
# 7) Find Total number of missing values
print(df.isna().sum())
print("*"*100)
#
# 8) Miss the missing value using proper method
#a) for trestbps
uniq=df['trestbps'].unique()
print(uniq)
print(df.dtypes)
print("*"*100)

x=df['trestbps'].mean()  # mean is usally use rather than median for the values property is unknown

# df['trestbps'].fillna(x,inplace=True)
df.fillna({'trestbps': x}, inplace=True)
print("Mean:",x)

# b) for restecg
x=df['restecg'].mode()[0]
# df['restecg'].fillna(x,inplace=True)
df.fillna({'restecg': x}, inplace=True)
print("Mode:",x)

#c)for thalach
x=df['thalach'].mean()
# df['thalach'].fillna(x,inplace=True)
df.fillna({'thalach': x}, inplace=True)
print("Mean:",x)

# d) for ca
x=df['ca'].mode()[0]
# df['ca'].fillna(x,inplace=True)
df.fillna({'ca': x}, inplace=True)
print("MOde:",x)


# e) for thal
x=df['thal'].mode()[0]
# df['thal'].fillna(x,inplace=True)
df.fillna({'thal': x}, inplace=True)
print("Mode:",x)
print(df.isna().sum())

# 9) trestbps  column above 150 data  wrong data
# x=df['trestbps'].median()
# for i in df.index:
#     if df.loc[i, 'trestbps'] >150 :
#         df.loc[i, 'trestbps'] = x
# print(df)

# HOW TO SAVE A FILE ?
df.to_csv('/Users/Acer/Downloads/heart_cleaned.csv',index=False)
print("Saved")
















# asm