#to change the order of the matrix

import numpy as np
a=np.array([[1,2,3,5],[1,2,5,6],[8,7,5,6]])
print(a)
# [[1 2 3 5]
#  [1 2 5 6]
#  [8 7 5 6]]

b=a.reshape([4,3])   # NO of element should be equal
print(b)
# [[1 2 3]
#  [5 1 2]
#  [5 6 8]
#  [7 5 6]]

b=a.reshape([2,6])   # NO of element should be equal
print(b)

# [[1 2 3 5 1 2]
#  [5 6 8 7 5 6]]