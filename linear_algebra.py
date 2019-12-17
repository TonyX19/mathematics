import numpy as np
from numpy.linalg import *

lst= np.eye(3)
print(lst)
'''
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''

# 矩阵的逆
print(inv(lst1))
# print(lst.invent)
'''
[[-2.   1. ]
 [ 1.5 -0.5]]
'''

# 转置矩阵
print(lst1.transpose())
'''
[[1 3]
 [2 4]]
'''

# 行列式
print(det(lst1))   # -2.0  determinant

# 特征值和特征向量
print(eig(lst1))   # eigenvalue
'''                 第一个元祖是特征值，第二个为对应的特征向量
(array([-0.37228132,  5.37228132]), array([[-0.82456484, -0.41597356],
       [ 0.56576746, -0.90937671]]))
'''

y = np.array([[5.],[7.]])         # 解方程组  注意括号

print(solve(lst1,y))
'''
[[-3.]
 [ 4.]]
'''

#一维向量和一维向量转置相乘

a = np.array([1,2])
# shape是查看数据有多少行多少列
a.shape[0] #列长度
a.shape[1] #行长度


print(a.shape)
t1 = a.reshape((len(a),1))
t2 = a.reshape((1,len(a)))

# reshape()是数组array中的方法，作用是将数据重新组织


print(t1.shape)
print(t2.shape)

b = np.dot(t1,t2)
print(b)
print(b.shape)

#一维转置
a = np.array([1,2,3,4,5])
a = a.reshape(a.shape[0],1)

#2nd way
mat_a = np.matrix([1,2,3,4])
print("matrix a: ", mat_a)
print("shape of a: ", mat_a.shape)

# transpose
mat_a_T = mat_a.T
print("matrix a'T: \n", mat_a_T)
print("shape of a'T: ", mat_a_T.shape)



#AᵀA的eigenvalue

A=np.array([[-1,2,-3],[4,-6,6]])
A_T=np.transpose(A)
Z=np.dot(A_T,A)
a,b=np.linalg.eig(Z) #其中a为特征值,b为特征向量


#array 运算
a1=array([1,1,1])  
a2=array([2,2,2])
a1*2                 #乘一个数

a1**3              #表示对数组中的每个数做平方

a1*a2 #数组点乘，相当于matlab点乘操作


a = np.zeros((2,2))  # Create an array of all zeros
print a              # Prints "[[ 0.  0.]
                     #          [ 0.  0.]]"
b = np.ones((1,2))   # Create an array of all ones
print b              # Prints "[[ 1.  1.]]"

c = np.full((2,2), 7) # Create a constant array
print c               # Prints "[[ 7.  7.]
                      #          [ 7.  7.]]"
d = np.eye(2)        # Create a 2x2 identity matrix
print d              # Prints "[[ 1.  0.]
                     #          [ 0.  1.]]"
e = np.random.random((2,2)) # Create an array filled with random values
print e                     # Might print "[[ 0.91940167  0.08143941]
                            #               [ 0.68744134  0.87236687]]"

#matrix 操作

m1 = np.matrix([1,2,3,4])
m[0]                #取一行
m[0,1]              #第一行，第2个数据


m1*m1.T             #注意左列与右行相等 m1.T为转置操作

multiply(m1,m2)     #执行点乘操作，要使用函数，特别注意

m.sort()                    #对每一行进行排序
m[1,:]                      #取得第一行的所有元素
m[1,0:1]                    #第一行第0个元素起1个元素，注意左闭右开
# matrix([[2]])
m[1,0:3]                    #第一行第0个元素起3个元素，注意左闭右开
# matrix([[2, 4, 6]])

#扩展矩阵函数tile()

x=np.matrix([0,0,0])
tile(x,(3,1))  #即将x扩展3个，j=1,表示其列数不变
# matrix([[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]])

tile(x,(2,2))  #x扩展2次，j=2,横向扩展
# matrix([[0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0]])






