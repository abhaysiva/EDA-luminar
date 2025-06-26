#arg sort

# to collect the index of the array in the sorted manner

import numpy as np

a=np.array([5,6,74,2,4,5,6,7]) #wt index : [0,1,2,3,4,5,6,7] ,sorted array:[ 2  4  5  5  6  6  7 74]
b=np.argsort(a)
print(b)  # sort the index of the sorted array
# [3 4 5 0 6 1 7 2]

a=np.array([[1,2,3,4,5],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)
# [[1 2 3 4 5]
#  [8 7 9 5 4]
#  [7 1 2 3 6]
#  [4 5 7 8 2]
#  [2 3 6 5 1]]
b=np.argsort(a) #row wise
print(b)
# [[0 1 2 3 4]
#  [4 3 1 0 2]
#  [1 2 3 4 0]
#  [4 0 1 2 3]
#  [4 0 1 3 2]]
b=np.argsort(a,axis=0) #col wise
print(b)
# [[0 2 2 2 4]
#  [4 0 0 0 3]
#  [3 4 4 1 1]
#  [2 3 3 4 0]
#  [1 1 1 3 2]]

