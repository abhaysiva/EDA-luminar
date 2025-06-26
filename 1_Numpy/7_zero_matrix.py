#zero
#matrix with all elements are zero
#[0,0,0,0]


#[0,0,0]
#[0,0,0]
#[0,0,0]


import numpy as np

# 2d
a=np.zeros([3,4],dtype=int) # because in default it will be float
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]
# 2
# (3, 4)
# 12


# 1d
a=np.zeros([5],dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [0 0 0 0 0]
# 1
# (5,)
# 5


#3d
a=np.zeros([1,4,5],dtype=int)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
# [[[0 0 0 0 0]
#   [0 0 0 0 0]
#   [0 0 0 0 0]
#   [0 0 0 0 0]]]
# 3
# (1, 4, 5)
# 20  ===>1*4*5
