#dot product
# condition: no: of the col of the first matrix and the no: of the rows of the second matrix should have to be equal

import numpy as np
a=np.array([[1,2,4],[2,5,4],[3,4,6]])
print(a)
# [[1 2 4]
#  [2 5 4]
#  [3 4 6]]

b=np.array([[5,6,3],[2,3,5],[4,5,2]])
print(b)
# [[5 6 3]
#  [2 3 5]
#  [4 5 2]]

# first element= sum of multiplication of the elements of the first row of the first matrix to elemnts of the first column of the second matrix

c=np.dot(a,b)
print(c)
# [[25 32 21]
#  [36 47 39]
#  [47 60 41]]

