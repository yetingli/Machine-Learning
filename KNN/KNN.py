#coding:utf-8
import csv
import random
import math
import operator
#KNN k-Nearest Neighbor 最邻近规则分类
class KNN:

    #初始化
    def __init__(self,num=1,split=0.67):
        self.k = num
        self.split = split #将数据集分为training set 和 tset set， training set 占2/3， test set 占1/3
        self.trainingSet = []
        self.testSet = []
        self.predictions = []

    #load dataset 加载数据
    def loadDataset(self,filename):
        self.trainingSet = []
        self.testSet = []
        with open(filename,'r') as csvifle: #with是对try…expect…finally语法的一种简化，并且提供了对于异常非常好的处理方式
            lines = csv.reader(csvifle) #从文件读取
            dataset = list(lines) # convert to a list
            for x in range(len(dataset)-1):
                for y in range(4):#5.1,3.5,1.4,0.2,Iris-setosa 五维数据 取前四个数据，即特征向量
                    dataset[x][y] = float(dataset[x][y])
                    #print dataset[x][y]
                if random.random()<self.split: #training set
                    self.trainingSet.append(dataset[x])
                else: # tset set
                    self.testSet.append(dataset[x])

    #计算距离 欧氏距离
    def euclideanDistance(self,instance1,instance2,length):#length 表示维度
        distance = 0
        for x in xrange(length):
            distance += math.pow((instance1[x]-instance2[x]),2)
        distance = math.sqrt(distance)
        return distance

    #计算k个Nearest Neighbors
    def getKNearestNeighbors(self,testInstance):
        distances = []
        length = len(testInstance)-1 #去掉标注
        for i in xrange(len(self.trainingSet)):
            dist = self.euclideanDistance(self.trainingSet[i],testInstance,length)
            distances.append((self.trainingSet[i],dist)) #元组形式
        distances.sort(key=operator.itemgetter(1)) #以第二个域进行排序，即距离排序
        neighbors = []
        for i in xrange(self.k):
            neighbors.append(distances[i][0])
        return neighbors

    #进行分类，少数服从多数
    def getResponse(self,neighbors):
        classVotes = {}
        for i in xrange(len(neighbors)):
            response = neighbors[i][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.iteritems(),key=operator.itemgetter(1),reverse=True)
        #classVotes.iteritems():返回字典键值对的元组集合
        #operator.itemgetter(1)：以第二域排序
        #reverse=True:降序
        return sortedVotes[0][0]

    #对测试集中每个实例进行预测
    def getPredictions(self):
        self.predictions = []
        for i in xrange(len(self.testSet)):
            neighbors = self.getKNearestNeighbors(self.testSet[i])
            result = self.getResponse(neighbors)
            self.predictions.append(result)

    #求预测的准确率
    def getAccuracy(self):
        correct = 0
        for i in xrange(len(self.testSet)):
            if self.testSet[i][-1] == self.predictions[i]:
                correct += 1
        return (correct/float(len(self.testSet)))*100.0

# test
if __name__ == "__main__":
    knn = KNN(3,0.67)
    knn.loadDataset('iris.data',)
    # print len(knn.trainingSet)
    # print len(knn.testSet)
    knn.getPredictions()
    print knn.getAccuracy()