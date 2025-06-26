from sklearn.neighbors import KNeighborsClassifier

# sklearn -package
# neighbors -module
# KNeighborsClassifier -funtion or object


# point position example

x1=[7,7,3,1]
y1=[7,4,4,4]

target=['BAD','BAD','GOOD','GOOD']  # output

# zip() : it is using for combining the two x axis and y axis ( here its going to store it in the variable -feature )

feature=list(zip(x1,y1))   #input
# we use list() for convert it into a list,because or it will be an object: <zip object at 0x000001F3CEE84680>

# print(feature)
# [(7, 7), (7, 4), (3, 4), (1, 4)]


# Model Creation

knn=KNeighborsClassifier(n_neighbors=3)
# knn -is the object created based on the KNeighborsCLassifier,which contains the distant Knn algorthms and distant formuls etc.
# n_neighbors=3 ,which means givig the value for K=3

knn.fit(feature,target) # training ,we passing the values input and output
print(knn.predict([[3,7]]))  #predict() is funtion using for the predit
# ['GOOD']

