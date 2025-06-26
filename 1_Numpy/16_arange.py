# arange - array range

# create a matrix with specific range

# arange funtion can create only 1 Dimention matrix.

import numpy as np
a=np.arange(1,11)
print(a)
# [ 1  2  3  4  5  6  7  8  9 10]
print('*'*100)

c=np.arange(1,11,2)
print(c) # 2 is the step
# [1 3 5 7 9]
print('*'*100)



# 1 to 20 elements (4,5)

b=np.arange(1,21)
print(b)
print('*'*100)
b=b.reshape([4,5])
print(b)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]
print('*'*100)


b=np.arange(1,21).reshape(4,5)    # we can use two funtion in single line
print(b)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]
print('*'*100)
d=np.arange(5,51,5).reshape([1,2,5])
print(d)



# [[[ 5 10 15 20 25]
#   [30 35 40 45 50]]]


print('*'*100)
d=np.arange(5,61,5).reshape([2,2,3])
print(d)
# [[[ 5 10 15]
#   [20 25 30]]
#
#  [[35 40 45]
#   [50 55 60]]]

