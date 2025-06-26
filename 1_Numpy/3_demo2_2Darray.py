import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print(a)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]]
print(a.ndim)
# 2
print(a.size)
# 15
print(a.shape)
# (3, 5)

b=np.array([[1,2,3,7],[4,5,6,8],[7,8,9,2]])
print(b)
# [[1 2 3 7]
#  [4 5 6 8]
#  [7 8 9 2]]
print(b.ndim)
# 2
print(b.size)
# 12
print(b.shape)
# (3,4)
