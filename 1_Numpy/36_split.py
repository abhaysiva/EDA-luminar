#split
import numpy as np
a=np.array([5,6,9,2,4,5,6,7,5,4,4,1,23,8,6,66])
print(a)

b=np.array_split(a,3)
print(b)
# [array([5, 6, 9, 2, 4, 5]), array([6, 7, 5, 4, 4]), array([ 1, 23,  8,  6, 66])]

b=np.array_split(a,3)
print(b[0])
# [5 6 9 2 4 5]

b=np.array_split(a,3)[0]
print(b) # split and collecting the one element from the splited array
# [5 6 9 2 4 5]

b=np.array_split(a,3)[0:2]
print(b)
# [array([5, 6, 9, 2, 4, 5]), array([6, 7, 5, 4, 4])]

