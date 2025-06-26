import pandas as pd
import numpy as np

df=pd.read_csv('/Users/Acer/Downloads/missing_data.csv')
print(df)
print(df.isna().sum())
print("*"*100)


# How to handle a wrong data?
# wrong data: Exceptional cases , like no chance that a data is will value in the dataset
# wrong data: Outlier ==>Used in ML

# eg:-

# height(cm)   Weight(kg)

# 169           75
# 178           70
# 171           65
# 400           900


# syntax:
# df.loc[index,'column name']=value

# df.loc[7,'Duration']=45
# print(df)



# if index is unknown, or big dataset
x=df['Calories'].mean()
for i in df.index:
    if df.loc[i, 'Calories'] >= 400:
        df.loc[i, 'Calories'] = x
print(df)

