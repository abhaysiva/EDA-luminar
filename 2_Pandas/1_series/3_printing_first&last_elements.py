import numpy as np
import pandas as pd
a=np.arange(1,51)
b=pd.Series(a)
print(b)
print("*"*100)


# print first 5 element
print(b.head())  #default 5 rows
print(b.head(3))
print(b.head(15))
print("*"*100)


#print last  5 elements
print(b.tail())
print(b.tail(3))
print(b.tail(15))

print(b.dtype) #int64