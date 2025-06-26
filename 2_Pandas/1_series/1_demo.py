#1D ==> Series

import pandas as pd
a=pd.Series([1,2,3,4,5])
print(a)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5


print(type(a))  # Datatype
# <class 'pandas.core.series.Series'>


print(a.ndim)   # dimension
# 1


print(a.shape)  # order
# (5,)


print(a.size)   # size
# 5

