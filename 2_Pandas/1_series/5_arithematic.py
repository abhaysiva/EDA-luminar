
import pandas as pd
a=pd.Series([3,4,5,1,6])
b=pd.Series([1,2,3,4,5])
c=a.add(b) #perform addition ,element by element
print(c)

# 0     4
# 1     6
# 2     8
# 3     5
# 4    11
# dtype: int64

a=pd.Series([3,4,5,1,6,8])
b=pd.Series([1,2,3,4,5])
c=a.add(b) #perform addition ,element by element
print(c)

# 0    2.0
# 1    2.0
# 2    2.0
# 3   -3.0
# 4    1.0
# 5    NaN
# dtype: float64

# here in NaN datatype is float


# substract
a=pd.Series([3,4,5,1,6])
b=pd.Series([1,2,3,4,5])
c=a.sub(b) #perform addition ,element by element
print(c)


#Multiple
c=a.mul(b)
print(c)

# Division
c=a.div(b)
print(c)
