
import numpy as np
a=np.ones([4,5],dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]
# 2
# (4, 5)
# 20


a=np.ones([8],dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [1 1 1 1 1 1 1 1]
# 1
# (8,)
# 8


a=np.ones([2,4,5],dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)


# [[[1 1 1 1 1]
#   [1 1 1 1 1]
#   [1 1 1 1 1]
#   [1 1 1 1 1]]
#                                   both are two set in the big matrix
#  [[1 1 1 1 1]
#   [1 1 1 1 1]
#   [1 1 1 1 1]
#   [1 1 1 1 1]]]


# 3
# (2, 4, 5)
# 40
