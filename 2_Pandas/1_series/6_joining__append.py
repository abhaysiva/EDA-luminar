
import pandas as pd
a=pd.Series([3,4,5,1,6])
b=pd.Series([1,2,3,4,5])

# join ==> append

c=a._append(b)
print(c)
# 0    3
# 1    4
# 2    5
# 3    1
# 4    6
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

c=a._append(b,ignore_index=True) # it is use for correcting the index
print(c)
# 0    3
# 1    4
# 2    5
# 3    1
# 4    6
# 5    1
# 6    2
# 7    3
# 8    4`
# 9    5
# dtype: int64

