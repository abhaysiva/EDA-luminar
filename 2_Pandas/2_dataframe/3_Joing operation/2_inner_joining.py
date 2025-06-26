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
# inner joining
df3=pd.merge(df1,df2,on='id',how='inner')
print(df3)
    # id  fname lname  age     prof  salary location
# 0  103   Amal     P   23  bigdata    1200    aluva
# 1  104  Binoy     U   27   python    2333  paravur
# 2  105  Vivek     V   22  flutter    4567   kollam

# Innner joining: join the rows ehich have the common values
