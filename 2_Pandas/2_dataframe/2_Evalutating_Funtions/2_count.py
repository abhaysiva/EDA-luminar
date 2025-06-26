# count

# newdfname = olddfname.groupby('colname') ['colname'].count()

import numpy as np
import pandas as pd

df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)

df1=df.groupby('prof')['prof'].count()
print(df1)
print("*"*100)

# sort based on the count of the each values in the specific col
df1=df.groupby('prof')['prof'].count()\
    .sort_values(ascending=False)   #in desecending manner
print(df1)
print("*"*100)

# heirarchy order : loc count sort colname head/tail

# if loc and iloc,for gettting rows from between ,we use iloc after loc ,mean in between the heirarchy
# collect the count  from the customer1 who work in differnet prof and also  the india
df1=df.loc[df['location']=='india']\
    .groupby('prof')['prof'].count()\
    .sort_values(ascending=False)   #in desecending manner
print(df1)
print("*"*100)

#collect the count of people work who work in diffent location
df1=df.groupby('location')['location'].count()\
    .sort_values(ascending=False)
print(df1)

df1=df.groupby('location')['location'].count()\
    .sort_values(ascending=False)
print(df1)


