#2 D slicing

import numpy as np
a=np.array([[1,2,3,4,5],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)
print('*'*100)
# [[1 2 3 4 5]
#  [8 7 9 5 4]
#  [7 1 2 3 6]
#  [4 5 7 8 2]
#  [2 3 6 5 1]]
# print(a[row slicing,column slicing])

print(a[1:3,:3])  #row=1,2  column =0,1,2
# [[8 7 9]
#  [7 1 2]]
print('*'*100)

print(a[:4,1:3])  #row=0,1,2,3  column =1,2
# [[2 3]
#  [7 9]
#  [1 2]
#  [5 7]]
print('*'*100)



print(a[1:4:2,1::2])
# [[7 5]
#  [5 8]]
print('*'*100)


print(a[:4:2,::2])
# [[1 3 5]
#  [7 2 6]]
print('*'*100)



# zeroth row of data
print(a[0])
# [1 2 3 4 5]
print('*'*100)


# sir method
print(a[0,:])
# [1 2 3 4 5]
#zeroth column of data
print('*'*100)

print(a[:,0])
# [1 8 7 4 2]
print('*'*100)

