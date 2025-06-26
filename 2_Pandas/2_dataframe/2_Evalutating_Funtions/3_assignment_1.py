import pandas as pd
import numpy as np

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

df2=df1.drop_duplicates()
print(df2)
print("*"*100)


# 1. Find Row count
print(df2.shape)
print("*"*100)


# 2. Remove duplicates rows and find total row count
df2=df1.drop_duplicates()
print(df2)
print(df2.shape)
print("*"*100)





# 3. Age maximum 10 fname,lname,prof,loc
df3=df2.sort_values(by='age',ascending=False) [['fname','lname','prof','location']].head(10)
print(df3)
print("*"*100)






# 4. Age minimum 5 employees fname,lname,prof,loc

df3=df2.sort_values(by='age') [['fname','lname','prof','location']].head(5)
print(df3)
print("*"*100)







# 5. Each location count [count desc order]
df3=df2.groupby('location')['location'].count()\
    .sort_values(ascending=False)
print(df3)
print("*"*100)









# 6. Full data
# df3=df2.loc[df2['location']=='australia']
# df3 = df2[df2['location'] == 'australia']

df3= df2.loc[df2['location']=='australia'][['id','fname','lname','age','prof','location']]
print(df3)
print("*"*100)





# 7. Each age group count [age desc order]
df3=df2.groupby('age')['age'].count()\
    .sort_values(ascending=False)
print(df3)
print("*"*100)








# 8. Each profession count [count desc order]
df3=df2.groupby('prof')['prof'].count()\
    .sort_values(ascending=False)
print(df3)
print("*"*100)





# 9.India work,A. Row count
df3=df2.loc[df2['location']=='india']
print(df3.shape)
print("*"*100)





# 9.India work,B. Each profession count [count desc order]
df3=df2.loc[df2['location']=='india'].groupby("prof")['prof'].count()\
    .sort_values(ascending=False)
print(df3)
print("*"*100)










# 9.India work,C. Age mxm 3 employees fname,lname,age,prof
df3=df2.loc[df2['location']=='india']\
    .sort_values(by='age',ascending=False)\
    .head(3)
print(df3)












# 9.India work,D. Age minimum 3 employees fname,lname,age,prof
df3=df2.loc[df2['location']=='india']\
    .sort_values(by='age')\
    [["fname",'lname','age','prof']]\
    .head(3)
print(df3)
print("*"*100)






# 9.India work,E. age above 40 full data
df3=df2.loc[df2['location']=='india']
df4=df3.loc[df3['age']>40]
print(df4)
print("*"*100)





# 9.India work,F. age range 30 to 40 [profession count]
df3=df2.loc[df2['location']=='india']
df4=df3.loc[(df3['age']>30) & (df3['age']<40)].groupby('prof')['prof'].count()
print(df4)
print("*"*100)










# 10 : us work
df3=df2.loc[df2['location']=='us']
print(df3)
print("*"*100)

# A. Row count
print(df3.shape)
print("*"*100)




# B. Each age group count
df4=df3.groupby('age')['age'].count()\
    .sort_values(ascending=False)
print(df4)
print("*"*100)









# C. Each profession count [count desc]
df4=df3.groupby("prof")["prof"].count().sort_values(ascending=False)
print(df4)
print("*"*100)












# D. Civil engineer dept and age above 30
df4 = df3.loc[(df3['prof'] == 'Civil engineer') & (df3['age'] > 30)]
print(df4)


