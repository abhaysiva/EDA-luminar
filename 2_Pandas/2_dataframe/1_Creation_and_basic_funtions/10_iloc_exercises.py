import pandas as pd
import numpy as np

df1=pd.read_csv('/Users/Acer/Downloads/customer1.txt',sep=',',header=None)
df1.columns=['id','fname','lname','age','prof','location']
print(df1)

print("*"*100)

# mainly use for collecting rows in between the data
#print every col and remove the last column

x=df1.iloc[:,0:5]
print(x)
print("*"*100)


x=df1.iloc[:,:-1] # print without last column
print(x)
print("*"*100)


#print only last col
y=df1.iloc[:,-1]
print(y)


# priority order
# loc column row

