# joi two array

import numpy as np
a=np.array([8,3,4,5,2,4,5])
b=np.array([9,5,6,7,2,37,4,4])
c=np.concatenate((a,b))
print(c)
# [ 8  3  4  5  2  4  5  9  5  6  7  2 37  4  4]
print("*"*100)

a=np.array([[1,2,3],[8,7,9],[7,1,6]])
print(a)
b=np.array([[5,2,3],[4,5,4],[5,1,2]])
print(b)

c=np.concatenate((a,b))
print(c)   #default of concatination is col wise
# [[1 2 3]
#  [8 7 9]
#  [7 1 6]
#  [5 2 3]
#  [4 5 4]
#  [5 1 2]]

c=np.concatenate((a,b),axis=1)
print(c)
# [[1 2 3 5 2 3]
#  [8 7 9 4 5 4]
#  [7 1 6 5 1 2]]
# eg:-

# file1
# id fname lname age
#file2
#  id fname lname age
# then axis=0



# file1
# id fname lname age
#file2
# prof salary dept location
# then axis=1

