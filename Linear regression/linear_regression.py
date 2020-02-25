import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


datasets = pd.read_csv("C:\\Users\\niraj\\Desktop\\house_prices.csv")
size = datasets['sqft_living']
x = np.array(size).reshape(-1,1)
price = datasets['price']
y = np.array(price).reshape(-1,1)

#Fitting a linear hyperplane using Linear Regression
model = LinearRegression()
model.fit(x, y)

#Calculate Mean error squared and chech r sqaure value to verify the accuarcy of Regression Model
mse = mean_squared_error(x, y)
r_squared_value = model.score(x,y)
print("Mean Squared Value is ", mse)
print("R squared value is ", r_squared_value)


#intercept is b0 and coefficient or slope is b1
b0 = model.intercept_[0]
b1 = model.coef_[0]
print(f"b0 is { model.intercept_[0]} and b1 is { model.coef_[0] }")

plt.scatter(x,y, color = 'red')
plt.plot(x, model.predict(x), color = 'green')
plt.title('Linear Regression')
plt.xlabel('Size of House')
plt.ylabel('Price of House')
plt.show()

#print(model.predict(x))
print(model.predict([[12344]]))

#The R squared value fpr Linear Regression model is very less the fitted model is not very accurate