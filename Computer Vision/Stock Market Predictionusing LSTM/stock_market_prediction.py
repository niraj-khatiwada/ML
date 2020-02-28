import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from matplotlib import pyplot as plt

dataset_train_load = pd.read_csv("C:/Users/niraj/Anaconda3/Projects/Computer Vision/Stock Market Predictionusing LSTM/SP500_train.csv")
dataset_test_load = pd.read_csv("C:/Users/niraj/Anaconda3/Projects/Computer Vision/Stock Market Predictionusing LSTM/SP500_test.csv")

# print("---", len(dataset_train_load['date']))
# print("---", len(dataset_test_load['date']))

train_dataset = dataset_train_load.iloc[:,5:6].values
test_dataset = dataset_test_load.iloc[:,5:6].values

#Use minmax normalization
print(train_dataset)
train_dataset = MinMaxScaler(feature_range=(0,1)).fit_transform(train_dataset)
# test_dataset = MinMaxScaler(feature_range=(0,1)).fit_transform(test_dataset)
#Now create a training dataset
X_train = []
y_train = []

for i in range(40, 1258):
    X_train.append(train_dataset[i-40:i, 0])
    y_train.append(train_dataset[i,0])

X_train = np.array(X_train)
y_train = np.array(y_train)

#There is particular shape to be apssed top LSTM architecture
#We have to reshape the data
#(numofSamples, numoffeatures,1), 1 beacuas our output is only for tommorrows
#numoffeatures past prices we used

X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

#Lets build LSTM model


model = Sequential()
model.add(LSTM(units=100,  return_sequences=True, input_shape=(X_train.shape[1], 1))) #return_sequence is treu beacause we are going to use LSTM model after this also this is false when we dont want to use LSTM next
model.add(Dropout(0.5))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(units=50))
model.add(Dropout(0.3))
model.add(Dense(units=1))

#USe loss function we are going to use Adam optimizer
model.compile(optimizer="adam", loss="mean_squared_error")
#fit the model

model.fit(X_train, y_train, epochs=100, batch_size=32)

# ------------ TESTING THE ALGORITHM ----------------
# training set plus testset
dataset_total = pd.concat((dataset_train_load['adj_close'], dataset_test_load['adj_close']),
                          axis=0)  # vertical axis=0 horizontal axis=1
# all inputs for test set
inputs = dataset_total[len(dataset_total) - len(dataset_test_load) - 40:].values
inputs = inputs.reshape(-1, 1)

# neural net trained on the scaled values we have to min-max normalize the inputs
# it is already fitted so we can use transform directly
inputs = train_dataset.transform(inputs)

X_test = []

for i in range(40, len(dataset_test_load) + 40):
    X_test.append(inputs[i - 40:i, 0])

X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

predictions = model.predict(X_test)

# inverse the predicitons because we applied normalization but we want to compare with the original prices
predictions = train_dataset.inverse_transform(predictions)

# plotting the results
plt.plot(test_dataset, color='blue', label='Actual S&P500 Prices')
plt.plot(predictions, color='green', label='LSTM Predictions')
plt.title('S&P500 Predictions with Reccurent Neural Network')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()


