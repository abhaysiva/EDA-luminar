# max

import numpy as np
a=np.array([5,6,74,2,4,5,6,7])
b=np.max(a)
print(b) #74

a=np.array([[1,2,3,4,5],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)
# [[1 2 3 4 5]
#  [8 7 9 5 4]
#  [7 1 2 3 6]
#  [4 5 7 8 2]
#  [2 3 6 5 1]]

b=np.max(a)
print(b)  #9

b=np.max(a,axis=0) # col wise
print(b) #[8 7 9 8 6]

b=np.max(a,axis=1) # row wise
print(b) #[5 9 7 8 6]



