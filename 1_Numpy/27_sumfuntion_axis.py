import numpy as np

a=np.array([1,2,3,4,5,6])
print(a)

b=np.sum(a)
print(b) #21

# in 2D
a=np.array([[1,2,3,4,5],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)

b=np.sum(a)
print(b) #110


#axis
# axis = 0 ,represent column
# axis = 1 ,represent row

b=np.sum(a,axis=0) # column sum
print(b)
# [22 18 27 25 18]

b=np.sum(a,axis=1) # row sum
print(b)
# [15 33 19 26 17]




