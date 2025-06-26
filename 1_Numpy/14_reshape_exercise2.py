import numpy as np
from numpy.ma.core import reshape

a=np.array([[7,8,9,5,4],[8,5,6,9,4],[1,2,5,4,6],[7,8,5,9,2]])
print(a)
# [[7 8 9 5 4]
#  [8 5 6 9 4]
#  [1 2 5 4 6]
#  [7 8 5 9 2]]

#1. 3 D (2,10)
#2. 1 D




print('*'*100)
b=a.reshape([1,2,10])
print(b)
# [[[7 8 9 5 4 8 5 6 9 4]
#   [1 2 5 4 6 7 8 5 9 2]]]




print('*'*100)
c=a.reshape([20])
print(c)
# [7 8 9 5 4 8 5 6 9 4 1 2 5 4 6 7 8 5 9 2]
