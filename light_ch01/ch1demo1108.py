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