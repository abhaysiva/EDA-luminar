import numpy as np
a=np.array([[1,2,3,6],[4,5,8,7],[7,1,2,3],[4,5,6,7]])
print(a)
# [[1 2 3 6]
#  [4 5 8 7]
#  [7 1 2 3]
#  [4 5 6 7]]

# 1.(2,8)
# 2. 3 dimention
# 3. 1 dimention

print()
b=a.reshape([2,8])
print(b)
# [[1 2 3 6 4 5 8 7]
#  [7 1 2 3 4 5 6 7]]

print()
c=a.reshape([2,4,2])  # only requirement is no of elements should have to be equal for the multiples
print(c)
# [[[1 2]
#   [3 6]
#   [4 5]
#   [8 7]]
#
#  [[7 1]
#   [2 3]
#   [4 5]
#   [6 7]]]

print()
d=a.reshape([16])
print(d)
# [1 2 3 6 4 5 8 7 7 1 2 3 4 5 6 7]
