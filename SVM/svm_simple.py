from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt


xBlue = np.array([0.3,0.5,1,1.4,1.7,2])
yBlue = np.array([1,4.5,2.3,1.9,8.9,4.1])

xRed = np.array([3.3,3.5,4,4.4,5.7,6])
yRed = np.array([7,1.5,6.3,1.9,2.9,7.1])

X = np.array([[0.3,1],[0.5,4.5],[1,2.3],[1.4,1.9],[1.7,8.9],[2,4.1],[3.3,7],[3.5,1.5],[4,6.3],[4.4,1.9],[5.7,2.9],[6,7.1]])
y = np.array([0,0,0,0,0,0,1,1,1,1,1,1]) # 0: blue class, 1: red class


plt.plot(xBlue, yBlue, 'bo')
plt.plot(xRed, yRed, 'ro')


classifier = svm.SVC()
classifier.fit(X, y)

predict = classifier.predict([[3,5]])
for i in predict:
    if i==1:
        plt.plot(3, 5, 'ro', markersize = 15)
    else:
        plt.plot(3,5, 'bo', markersize = 15)

print("Prediciton is :",predict)
plt.show()