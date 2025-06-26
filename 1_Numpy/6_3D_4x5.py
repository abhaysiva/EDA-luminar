#3d 4*5
import numpy as np
a=np.array([[[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8]]])
print(a)
# [[[1 2 3 4 5]
#   [2 3 4 5 6]
#   [3 4 5 6 7]
#   [4 5 6 7 8]]]
print(a.ndim)
# 3
print(a.shape)
# (1, 4, 5)
print(a.size)
# 20  ====>1*4*5


