import sys, os
import numpy as np
sys.path.append(os.pardir)  # 为了导入父目录的文件而进行的设定
from dataset.mnist import load_mnist
from PIL import Image
import pickle
# 2019年11月9日19:07:39、
# 输出各个数据的形状
# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)
# def img_show(img):
#     pil_img=Image.fromarray(np.uint8(img)) #将保存的图像数据转为PIL的数据对象
#     pil_img.show()
# (x_train, t_train), (x_test, t_test)=load_mnist(flatten=True, normalize=False)
# img=x_train[0]
# label=t_train[0]
# print(label)
# print(img.shape) #784
# img=img.reshape(28,28)
# print(img.shape)
# img_show(img)
def sigmoid(x):
    return 1/(1+np.exp(-x))
def softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return  y
def get_data():
    (x_train,t_train),(x_test,y_test)=load_mnist(normalize=True,flatten=True,one_hot_label=False)
    return x_test, y_test

def init_network():
    with open("sample_weight.pkl",'rb') as f :
        network=pickle.load(f)
        return network

def predict(network,x):
    W1,W2,W3=network['W1'],network['W2'],network['W3']
    b1,b2,b3=network['b1'],network['b2'],network['b3']
    a1=np.dot(x,W1)+b1
    z1=sigmoid(a1)
    a2=np.dot(z1,W2)+b2
    z2=sigmoid(a2)
    a3=np.dot(z2,W3)+b3
    y=softmax(a3)
    return y

x,t=get_data()
network=init_network()

accuracy_cnt=0
for i in range(len(x)): # len(x) all sample number
    y=predict(network,x[i])
    p=np.argmax(y)
    if p==t[i]:
        accuracy_cnt+=1
print("accuracy"+str(float(accuracy_cnt)/len(x)))
