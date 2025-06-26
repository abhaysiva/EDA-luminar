# Whatsapp questions by sir

# 1) fname,lname,age,prof,location
# 2) Age above 50 fname,lname,age,prof
# 3) Age less than 30 fname,lname,age,prof,loc
# 4) Age above 50 and work india fname,lname,age,prof
# 5) Age mxm 5 employee fname,lname,age,prof
# 6) Ahe min 3 emp fname,lname,age,prof
# 7) india work fname,lname,age,prof
# 8) india work and age above 50 fname,lname,age,prof
# 9) india work, age mxm 2 emp fname,lname,age
# 10) india work, age min 1 emp fname,lname,age
# 11) pilot prof, age mxm 1 emp fname,lname,age
# 12) us work and age above 50 fname,lname,age
# 13) uk work age min 3 emp fname,lname,age,prof



import numpy as np
import pandas as pd

df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)






#cleaning data
#finding missing value
print(df.isna().sum())
print("*"*100)
# fill the missing value with india
print("fill the missing value with india")
print("*"*100)
df1=df.fillna('india')
print(df1.isna().sum())



print("*"*100)
# 1.1) fname,lname,age,prof,location

df1=df [['fname','lname','age','prof','location']]
print(df1)

# df1=df.iloc[:,1:]
# print(df1)
print("*"*100)

# 2. Age above 50 fname,lname,age,prof

df1=df.loc[df['age']>50] [['fname','lname','age','prof']]
print(df1)
print("*"*100)

#3.Age less than 30 fname,lname,age,prof,loc
df1=df.loc[df['age']<30] [['fname','lname','age','prof','location']]
print(df1)
print("*"*100)


#4. Age above 50 and work india fname,lname,age,prof
df1 = df.loc[(df['age'] < 30) & (df['location'] == 'india'), ['fname', 'lname', 'age', 'prof', 'location']]
print(df1)
print("*" * 100)



# 5) Age mxm 5 employee fname,lname,age,prof

df1=df.sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head(5)
print(df1)
print("*"*100)

# 6.6) Age min 3 emp fname,lname,age,prof
df1=df.sort_values(by='age') [['fname','lname','age','prof']].head(3)
print(df1)
print("*"*100)

# 7.7) india work fname,lname,age,prof

df1 =df.loc[df['location'] == 'india'] [['fname', 'lname', 'age', 'prof', 'location']]
print(df1)
print("*" * 100)


# 8) india work and age above 50 fname,lname,age,prof

df1 = df.loc[(df['age'] >50) & (df['location'] == 'india'), ['fname', 'lname', 'age', 'prof', 'location']]
print(df1)
print("*" * 100)

# 9.india work, age mxm 2 emp fname,lname,age

df1=df.loc[df['location']=='india'].sort_values(by='age',ascending=False) [['fname','lname','age',]].head(2)
print(df1)
print("*"*100)

#10.india work, age min 1 emp fname,lname,age
df1=df.loc[df['location']=='india'].sort_values(by='age') [['fname','lname','age']].head(1)
print(df1)
print("*"*100)

# 11.Pilot prof, age mxm 1 emp fname,lname,age

df1=df.loc[df['prof']=='Pilot'].sort_values(by='age',ascending=False) [['fname','lname','age']].head(1)
print(df1)
print("*"*100)

#.12) us work and age above 50 fname,lname,age

df1 = df.loc[(df['age'] >50) & (df['location'] == 'us'), ['fname', 'lname', 'age']]
print(df1)
print("*" * 100)

#13.uk work age min 3 emp fname,lname,age,prof
df1=df.loc[df['location']=='uk'].sort_values(by='age') [['fname','lname','age','prof']].head(3)
print(df1)
print("*"*100)