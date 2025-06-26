import numpy as np

#2d 5*4

a=np.array([[1,2,3,4],[5,2,3,6],[7,8,5,9],[1,4,5,6],[7,8,9,6]])
print(a)
# [[1 2 3 4]
 # [5 2 3 6]
 # [7 8 5 9]
 # [1 4 5 6]
 # [7 8 9 6]]
print(a.ndim)
# 2
print(a.size)
# 20
print(a.shape)
# (5,4)
print(a.shape[0]*a.shape[1])

