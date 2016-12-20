#coding:utf-8

from sklearn import neighbors
from sklearn import datasets


knn = neighbors.KNeighborsClassifier()

#  target_names
# 'setosa', 'versicolor', 'virginica'
#   0           1           2

iris = datasets.load_iris()

#print iris

knn.fit(iris.data, iris.target)
#让knn建立模型

predictedLabel = knn.predict([[0.1,0.2,0.3,0.4]])
print predictedLabel