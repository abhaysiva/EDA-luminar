import numpy as np
import pandas as pd

a=pd.Series((3,4,5,1,6,7,8,5,2,3,4,5),dtype=float)
print(a)
print(a.ndim)   # dimension
print(a.shape)  # order
print(a.size)   # no: of elements
print(type(a))  #type
print("*"*100)

a=pd.Series({1:54,2:56,3:75,4:58})
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(type(a))
print("*"*100)

a=pd.Series({'id':101,'name':'abhay','age':23,"location":'aluva'}) # here in dicitionary key value pair act as index
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(type(a))
print("*"*100)

