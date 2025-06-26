# full matrix

# every element of the matrix should have to be one particular digit

#[6,6,6,6]


#[3,3,3]
#[3,3,3]
#[3,3,3]
import numpy as np
a=np.full([4,5],3)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [[3 3 3 3 3]
#  [3 3 3 3 3]
#  [3 3 3 3 3]
#  [3 3 3 3 3]]
# 2
# (4, 5)
# 20

a=np.full([1,3,4],7)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [[[7 7 7 7]
#   [7 7 7 7]
#   [7 7 7 7]]]
# 3
# (1, 3, 4)
# 12

a=np.full([8],5)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [5 5 5 5 5 5 5 5]
# 1
# (8,)
# 8
