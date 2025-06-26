import numpy as np
a=np.array([8,3,4,6,5,9,7,8])

b=np.sort(a) # sort in ascending order

print(b)
print("*"*100)


# print in reverse order

# b=np.sort(a)[::-1]
b=np.sort(a)
print(b[::-1])
print("*"*100)


#in 2D
# in default it is sort based on the row
a=np.array([[5,2,6,4,7],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)
# [[5 2 6 4 7]
#  [8 7 9 5 4]
#  [7 1 2 3 6]
#  [4 5 7 8 2]
#  [2 3 6 5 1]]
print("*"*100)

b=np.sort(a) #sort based on row ==>default or using axis=1
print(b)
# [[2 4 5 6 7]
#  [4 5 7 8 9]
#  [1 2 3 6 7]
#  [2 4 5 7 8]
#  [1 2 3 5 6]]
print("*"*100)




b=np.sort(a,axis=0) #sort based on column wise
print(b)
# [[2 1 2 3 1]
#  [4 2 6 4 2]
#  [5 3 6 5 4]
#  [7 5 7 5 6]
#  [8 7 9 8 7]]
print("*"*100)


# row wise reverse order
b=np.sort(a)[::,::-1] #sort based on row
print(b)
print("*"*100)
# [[7 6 5 4 2]
#  [9 8 7 5 4]
#  [7 6 3 2 1]
#  [8 7 5 4 2]
#  [6 5 3 2 1]]



# col wise reverse order
b=np.sort(a,axis=0)[::-1,::] #sort based on column wise
print(b)
# [[8 7 9 8 7]
#  [7 5 7 5 6]
#  [5 3 6 5 4]
#  [4 2 6 4 2]
#  [2 1 2 3 1]]