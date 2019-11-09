# step_function
import numpy as np
import matplotlib.pyplot as plt
def setp_function(x):
    return np.array(x>0,dtype=np.int)
# 可以用 astype()方法转换NumPy数组的类型。 astype()方
# 法通过参数指定期望的类型，这个例子中是 np.int型。
x=np.arange(-5,5,0.1)
y=setp_function(x)

plt.ylim(-0.1, 1.1)
plt.title('step_function')
# plt.show()
# ------------------------------
# sigmoid_function
def sigmoid(x):
    return 1/(1+np.exp(-x))
x=np.arange(-5,5,0.1)
y=sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.title('sigmoid_function')
# plt.show()
# ------------------------------
# discuss the different between sigmoid and step function
# 当输入信号为重要信息时，阶跃函数和sigmoid函数都会输出较大的值；
# 当输入信号为不重要的信息时，两者都输出较小的值。
# 还有一个共同点是，不管输入信号有多小，或者有多
# 大，输出信号的值都在0到1之间。
# 两者均为非线性函数。sigmoid函数是一条曲线，
# 阶跃函数是一条像阶梯一样的折线，两者都属于非线性的函数
# 神经网络的激活函数必须使用非线性函数
# 线性函数的问题在于，不管如何加深层数，总是存在与之等效的 “无隐藏层的神经网络”
# 使用线性函数时，无法发挥多层网络带来的优势。
# 因此，为了发挥叠加层所带来的优势，激活函数必须使用非线性函数。
# ------------------------------
# Relu_function
# ReLU函数在输入大于0时，直接输出该值；在输入小于等于0时，输
# 出0
def relu(x):
    return np.maximum(0,x)
# Numpy dot
A=np.array([[1,2],[3,4]])
A.shape
B=np.array([[5,6],[7,8]])
B.shape
print(np.dot(A,B))
# ----
# NN dot
X=np.array([1,2])
W=np.array([[1,3,5],[2,4,6]])
print(np.dot(X,W))
##
#
# 三层神经网络
# 3.4.1 in page57
# softmax function
def softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return  y
