import numpy as np
a=np.array([5,6,9,2,4,5,6,7])
print(a)

b=np.argmax(a)
print(b) #2: index of highest element

b=np.argmin(a)
print(b) #3: index of lowest element


a=np.array([[1,2,3,4,5],[8,7,9,5,4],[7,1,2,3,6],[4,5,7,8,2],[2,3,6,5,1]])
print(a)


b=np.argmax(a)
print(b) #7 :index count from the first row and select the second row and so on,
        #THE WE get count 8 for the highest element ,but index 8-1=7

b=np.argmax(a,axis=0) #col wise ,index of highest element
print(b) #[1 1 1 3 2]


b=np.argmax(a,axis=1) #row wise ,index of highest element
print(b) #[4 2 0 3 2]


b=np.argmin(a,axis=0) #col wise ,index of lowest element
print(b) #[0 2 2 2 4]


b=np.argmin(a,axis=1) #row wise ,index of lowest element
print(b) #[0 4 1 4 4]

