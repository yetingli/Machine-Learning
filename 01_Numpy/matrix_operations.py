#coding:utf-8
'''''''''''''''''''''''''''''''''''''''''''''
Numpy是Python的一个矩阵类型，提供大量矩阵处理
的函数，它内部运算是通过C语言而不是Python实现
Numpy包含两种基本的数据类型：数组和矩阵
'''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''
        array运算
'''''''''''''''''''''''''''''
from numpy import array
mm = array((1,2,3))
pp = array((1,1,1))
arr3 = array((0.3,0.2,0.3))
print type(mm)
print mm
print pp+mm #add
print pp-mm #sub
print mm*2 #mul
print mm**2 #平方
print pp[1] #访问数组里的元素
jj = array([[1,2,3],[1,1,1]])#二维数组
print jj
print jj[0,1] #jj[0][1]这样也可以
print mm*arr3 # 两个数组的元素对应相乘 1*4 2*5 3*6

'''''''''''''''''''''''''''''
        matrix运算
'''''''''''''''''''''''''''''
from numpy import mat,matrix #关键词mat是matrix的缩写
ss = mat([1,2,3])
print type(ss)
print ss
ss2 = matrix([1,2,3])
print type(ss2)
print ss2
#print ss2[0,2] #访问矩阵第一行第三个元素
#print ss2[0][1] #这样不行
print ss*ss2.T #转置 1*3 3*1
print ss.T*ss2
'''''''''''''''''
1   1 2 3   1 2 3
2           2 4 6
3           3 6 9
'''''''''''''''''
list1 = [5,11,1605]
ss3 = mat(list1)
print ss3
print mat([5,11,1605])

'''''''''''
矩阵大小
'''''''''''
from numpy import shape
size = shape(ss3)
print size

'''''''''''''''''
矩阵每个元素对应相乘
'''''''''''''''
from numpy import multiply
print multiply(ss,ss2)

'''''
矩阵排序
sort:原地排序（即排序后的结果占用原始的存储空间）
     希望保留原始数据的原序，必须实现做一份拷贝
argsort:得到矩阵中每个元素的排序序号
'''''
ss4 = mat([4,5,1])
ss4.sort() #矩阵排序
print ss4
ss4 = mat([4,5,1]) # print 2 0 1
print ss4
print ss4.argsort()
print ss4

print ss4.mean()#求均值

jj = mat([[1,2,3],[8,8,8]])
print type(jj)
print shape(jj)#行和列
print type(shape(jj))
print shape(jj)[0] #行
print shape(jj)[1] #列

print jj[0,:]
print jj[1,:]
print jj[0,0:2]#半开半闭区间

from numpy import *
a = random.rand(4,4)
print a

b = random.randint(5, size=(3, 3))#整数
print b
# print type(b)
# print b
# print type(mat(b))
b = mat(b)
#print array(b)

print b.T
print b.I #矩阵的逆
print b
print b * b.I