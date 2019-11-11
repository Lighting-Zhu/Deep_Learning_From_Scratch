import sys,os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient
class simpleNet:
    def __init__(self):
        self.w=np.random.randn(2,3)# 用高斯分布做初始化
    def predict(self,x):
        return np.dot(x,self.w)
    def loss(self,x,t):
        z=self.predict(x)
        y=softmax(z)
        loss=cross_entropy_error(y,t)
        return loss
net=simpleNet()
print(net.w) #权重参数

x=np.array([0.6,0.9])
p=net.predict(x)
print(p)
print(np.argmax(p))
true_label=np.array([0,0,1])
net.loss(x,true_label)
print(net.loss(x,true_label))