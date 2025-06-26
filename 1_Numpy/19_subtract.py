#Subtraction
import numpy as np
a=np.array([[1,2,4],[2,5,4],[3,4,6]])
print(a)

b=np.array([[5,6,3],[2,3,5],[4,5,2]])
print(b)

c=np.subtract(a,b)
print(c)
# [[-4 -4  1]
#  [ 0  2 -1]
#  [-1 -1  4]]
