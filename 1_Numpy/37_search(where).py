# search

# where
import numpy as np
a=np.array([5,6,9,2,4,5,6,7,5,4,4,1,23,8,6,66])
print(a)

b=np.where(a==5)
print(b) # return the array of index where the elements is present
# (array([0, 5, 8]),)

a=np.array([[1,2,3,4,5],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)

b=np.where(a==5)
print(b) # print the details of the elements row position and col position
# (array([0, 1, 3, 4]), array([4, 3, 1, 3]))

