#coding:utf-8
''''
sum:求和
mean:均值
var:方差
cov:协方差
std:标准差
'''''
import numpy
from numpy import random
from numpy import mat
import matplotlib
import matplotlib.pyplot as plt
b = random.randint(5, size=(2, 3))#整数
b = mat(b)
print b

#求和 均值
print b.sum()
print b.mean()
# print b.sum(axis=0)#二维数组 就俩数轴
# print b.mean(axis=0)
# print b.sum(axis=1)
# print b.mean(axis=1)
# print b.sum(axis=-1)


#方差 标准差 协方差
print b.var()
print b.std()
#print b.cov()
''''
4 1 2
4 0 4
1 4 1
'''
'''
4+1+2+4+0+4+1+4+1=21
21/9=7/3=2.3333333
'''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(b[0,:],b[1,:])
#ax.scatter(b[:,0],b[:,1])
plt.show()