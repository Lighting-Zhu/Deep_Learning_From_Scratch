# ch2 perceptron
# 2019年11月9日10:19:10
# 逻辑门的实现
# AND 和门
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    tmp=x1*w1+x2*w2
    if tmp<=theta:
        return 0
    elif tmp>theta:
        return 1
# test example
y1=AND(0,0)
y2=AND(1,0)
y3=AND(0,1)
y4=AND(1,1)

ax = plt.axes(projection='3d')
ax.scatter3D(0, 0, y1, 'gray')
ax.scatter3D(1, 0, y2, 'gray')
ax.scatter3D(0, 1, y3, 'gray')
ax.scatter3D(1, 1, y4, 'gray')
# plt.show()

# 导入权重与偏置
x=np.array([0,1])
w=np.array([0.5,0.5])
b=-0.7
print(w*x)
y=np.sum(w*x)+b
print(y)

# NAND
def NAND(x1,x2)
    x=np.array([x1,x2])
    w=np.array([-0.5,-0.5])
    b=0.7
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
def OR(x1,x2)
    x=np.array([x1,x2])
    w=np.array([0.5,0.5])
    b=-0.2
    tmp=np.sum(w*x)+b
    if tmp<=0:
        return 0
    else:
        return 1
