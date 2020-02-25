import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import math
import matplotlib.pyplot as plt

x1 = np.array([0,0.6,1.1,1.5,1.8,2.5,3,3.1,3.9,4,4.9,5,5.1])
y1 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0])

x2 = np.array([3,3.8,4.4,5.2,5.5,6.5,6,6.1,6.9,7,7.9,8,8.1])
y2 = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1])

X = np.array([[0],[0.6],[1.1],[1.5],[1.8],[2.5],[3],[3.1],[3.9],[4],[4.9],[5],[5.1],[3],[3.8],[4.4],[5.2],[5.5],[6.5],[6],[6.1],[6.9],[7],[7.9],[8],[8.1]])
Y = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])

plt.plot(x1, y1,'ro', color = 'red' )
plt.plot(x2, y2, 'bo', color = 'blue')


model = LogisticRegression()
model.fit(X, Y)

b0 = model.intercept_
b1 = model.coef_
print("b0 value= ",b0 )
print("b1 value= ",b1)

class LogisticFunction():
    def logistic_function(self, b0, b1, x):
        p = (1 / (1 + np.exp(-(b0 + b1 * x))))
        # print(p)
        return p
ins = LogisticFunction()
for i in range(1,120):
    plt.scatter(i/10 ,ins.logistic_function(b0, b1, i/10), color = 'green')

plt.axis([-2,10, -0.5, 1.5])


print("prediciton is ",model.predict([[5]]) )
a = model.predict([[5]])
for i in a:
    plt.plot(5, a, 'ko')

plt.show()