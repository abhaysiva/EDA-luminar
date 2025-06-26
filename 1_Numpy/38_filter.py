# filter  (concept)

import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])


b=a>6
c=a[b]
print(c)
# [ 7  8  9 10 11 12 13]
print("*"*100)


a=np.arange(1,51)
b=a%2==0
c=a[b]
print(c)

