# identity matrix

# if all the diagonal elements are 1 and all the other elements are zero ,
# and the matrix should have to be square matix,no: of rows equal to no:of columns,
# then it is indentity matrix.

# [1,0,0]
# [0,1,0]
# [0,0,1]

# [1] is not identity matirx

#[1,0,0]
#[0,1,0] in not a identity matrix


import numpy as np

a=np.identity(5,dtype=int)
print(a)
# [[1 0 0 0 0]
#  [0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]
#
a=np.eye(3,dtype=int)
print(a)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]

