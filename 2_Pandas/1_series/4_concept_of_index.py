import numpy as np
import pandas as pd

a=pd.Series({'id':101,'fname':'abhay','lname':'siva','age':23,'prof':'Engineer',"salary":10000},
            index=['fname','age','lname','id','salary','prof'])
#we can reorder the elements in the printing(index changing and corrensponding element is also changing)
print(a)

# fname        abhay
# age             23
# lname         siva
# id             101
# salary       10000
# prof      Engineer
# dtype: object


print('*'*100)
a=pd.Series((3,4,5,1,2,3,4,5),index=[7,0,3,4,5,1,6,2])
print(a) # but here there is only change in the index not in the corresponding element

# 7    3
# 0    4
# 3    5
# 4    1
# 5    2
# 1    3
# 6    4
# 2    5
# dtype: int64




