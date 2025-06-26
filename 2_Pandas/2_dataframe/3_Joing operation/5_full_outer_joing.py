import numpy as np
import  pandas as pd

dic1={'id':[101,102,103,104,105],'fname':['Vinay','Anu','Amal','Binoy','Vivek'],'lname':['K','S','P','U','V'],'age':[28,24,23,27,22]}
dic2={'prof':["bigdata","python","flutter","bigdata","python"],'id':[103,104,105,106,107],'salary':[1200,2333,4567,1230,9123],'location':["aluva","paravur","kollam","karumaloor","Mannam"]}


df1=pd.DataFrame(dic1)
print(df1)
    # id  fname lname  age
# 0  101  Vinay     K   28
# 1  102    Anu     S   24
# 2  103   Amal     P   23
# 3  104  Binoy     U   27
# 4  105  Vivek     V   22

df2=pd.DataFrame(dic2)
print(df2)
      # prof   id  salary    location
# 0  bigdata  103    1200       aluva
# 1   python  104    2333     paravur
# 2  flutter  105    4567      kollam
# 3  bigdata  106    1230  karumaloor
# 4   python  107    9123      Mannam
print("*"*100)

df3=pd.merge(df1,df2,on='id',how='outer')
print(df3)


    # id  fname lname   age     prof  salary    location
# 0  101  Vinay     K  28.0      NaN     NaN         NaN
# 1  102    Anu     S  24.0      NaN     NaN         NaN
# 2  103   Amal     P  23.0  bigdata  1200.0       aluva
# 3  104  Binoy     U  27.0   python  2333.0     paravur
# 4  105  Vivek     V  22.0  flutter  4567.0      kollam
# 5  106    NaN   NaN   NaN  bigdata  1230.0  karumaloor
# 6  107    NaN   NaN   NaN   python  9123.0      Mannam


# full outer join:
# join the bothe comman value and remaining will be null