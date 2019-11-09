a=[1,2,3]
print(a[0:-1])
# dictionary
me={'height':180}
me['weight']=70
print(me)

#---
class Man:
    def __init__(self, name):
        self.name= name
        print("Initialized")
    def hello(self):
        print("hello"+ self.name +"!")

m=Man("David")
m.hello()
#---
import numpy as np
# 生成 numpy是数组
x=np.array([1,2,3])
print(x)
y=np.array([2,3,4])
print(x+y)
print(x-y)
print(x*y)

X=np.array([[51,55],[14,19],[2,7]])
print(X[0][1])
print(X.flatten())
# ch1 is end
# ch 1.5


#%%
import numpy as np
import matplotlib.pyplot as plt
# 生成数据
x= np.arange(0,6,0.1) # step length 0.5,range[0,6]
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y1,label='sin')
plt.plot(x, y2, label='cos')
plt.xlabel('x')
plt.xlabel('y')
plt.title('sin & cos')
plt.legend()
plt.show()

import matplotlib.pyplot as plt
from matplotlib.image import imread
img=imread('test.png')
plt.imshow(img)
plt.show()
