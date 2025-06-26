# print each elements in the array

import numpy as np
a=np.array([5,6,9,2,4,5,6,7])
print(a)
for i in a:
    print(i)

print('*'*100)
a=np.array([[1,2,3,4,5],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)
for i in a:
    for j in i:
        print(j)


