# max()
# finding max value of the column corresponding to the another column

import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df.columns=['id','fname','lname','age','prof','location']
print(df)
print("*"*100)


# newdfname = olddfname.groupby('colname1')['colname2'].max()
df1=df.groupby('prof')['age'].max()
print(df1)
print("*"*100)

# group by colname1 and select by colname2
#eg :- group by prof and select by age
#eg2:- group by location and select by salary

#and sorting it by sort_values
#if we dont use sort_values then it will order by alphabetic order of the prof
df1=df.groupby('prof')['age'].max()\
    .sort_values(ascending=False)
print(df1)
print("*"*100)









