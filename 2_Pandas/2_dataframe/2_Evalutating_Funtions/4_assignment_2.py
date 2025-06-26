import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)

df=pd.read_csv('/Users/Acer/Downloads/movies_cleaned_pandas.csv',sep=',',header=None)
df.columns=['S.No','Name','Year','Ratings','Runtime']
print(df)

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



# 1. Find row count
print(df2.shape)



# 2.Remove duplicates and find row count
df2=df1.drop_duplicates()
print(df2)
print("*"*100)
print(df2.shape)



# 3.Sort data set by release year in des order
df3=df2.sort_values(by='Year',ascending=False)
print(df3)
print("*"*100)



#4.Find rating mxm 5 movies name,year,rating
df3=df2.sort_values(by='Ratings',ascending=False)[['Name','Year','Ratings']].head(5)
print(df3)
print("*"*100)



# 5:Find rating minimum 3 movies name,year,rating

df3=df2.sort_values(by='Ratings')[['Name','Year','Ratings']].head(3)
print(df3)
print("*"*100)



#6:Find Each year release movie count [count desc order]
df3=df2.groupby('Year')['Year'].count().sort_values(ascending=False)
print(df3)
print("*"*100)


# 7:Each rating count [count desc order]
df3=df2.groupby('Ratings')['Ratings'].count().sort_values(ascending=False)
print(df3)
print("*"*100)



#8:2008 and rating above 3 [collect], row count
df3=df2.loc[(df2['Year']==2008) & (df2['Ratings']>3)]
print(df3.shape)
print("*"*100)



#9:Find duration mxm 1 movies name,year,rating,duration
df3=df2.sort_values(by='Runtime',ascending=False).head(1)
print(df3)
print("*"*100)





 #10:Find rating min 1 movies name,year,rating,duration
df3=df2.sort_values(by='Ratings').head(1)
print("*"*100)








# 11. Rating above 4 and relase year above 2005
# A. Rating mxm movies full data

df3=df2.loc[(df2['Ratings']>4) & (df2['Year']>2005)]
print(df3)
df4=df3.sort_values(by='Ratings',ascending=False).head(1)
print(df4)
print("*"*100)




# 11. Rating above 4 and relase year above 2005
# B. Rating mnm movies full data
df3=df2.loc[(df2['Ratings']>4) & (df2['Year']>2005)]
print(df3)
df4=df3.sort_values(by='Ratings').head(1)
print(df4)
print("*"*100)




# 12. 2008 movies count
df3=df2.loc[df2["Year"]==2008].groupby('Year')['Year'].count()
print(df3)
print("*"*100)






# 13. 1975-2000 movies collect
# A. Row count
df3 = df2.loc[(df2['Year'] >= 1975) & (df2['Year'] <= 2000)]
row_count = df3.shape[0]  # Get the number of rows
print("NO: OF ROWS:",row_count)
print("*"*100)





# 14. 1975-2000 and rating above 3.5 total row count
df3 = df2.loc[(df2['Year'] >= 1975) & (df2['Year'] <= 2000) & (df2['Ratings']>3.5)]
row_count = df3.shape[0]  # Get the number of rows
print("NO: OF ROWS:",row_count)




