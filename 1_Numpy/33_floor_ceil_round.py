# floor ceil and round

import numpy as np

a=np.array([[7.5,5.8,9.8,2.4],[4.5,5.3,4.5,4.3],[3.4,4.5,5.9,3.2],[3.4,2.4,5.4,4.3]])
print(a)
# [[7.6 5.8 9.8 2.4]
#  [4.5 5.3 4.3 4.3]
#  [3.4 4.5 5.9 3.2]
#  [3.4 2.4 5.4 4.3]]


#floor  ===> chooose the lowest part ,means 5.9==>5,8.6===>8
b=np.floor(a)
print(b)
# [[7. 5. 9. 2.]
#  [4. 5. 4. 4.]
#  [3. 4. 5. 3.]
#  [3. 2. 5. 4.]]



#ceil
# reverse operation of floor,chooose the highest part ,means 5.9==>6,8.6===>9

b=np.ceil(a)
print(b)
# [[ 8.  6. 10.  3.]
#  [ 5.  6.  5.  5.]
#  [ 4.  5.  6.  4.]
#  [ 4.  3.  6.  5.]]



# Round

#.5 above ==>highest
#.5 below ==>lowest


#.5 odd number==> highest
#.5 even number ==>lowest

b=np.round(a)
print(b)

# [[ 8.  6. 10.  2.]
#  [ 4.  5.  4.  4.]
#  [ 3.  4.  5.  3.]
#  [ 3.  2.  5.  4.]]


