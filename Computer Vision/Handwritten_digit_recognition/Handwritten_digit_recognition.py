from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, Dense
from keras.layers import Activation, MaxPooling2D, Flatten, BatchNormalization, Dropout
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.utils import  np_utils

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# print(len(x_train), len(x_test), x_train.shape, x_test.shape) #these are images so 28*28
# print(x_test.shape) #Test is also image ofcourse
# print(y_test) #The main output is number so this is integer value from 0-9

# plt.imshow(x_test[10], cmap='gray')

#We have to reshape the data first

features_train = x_train.reshape(len(x_train), 28, 28, 1)
features_test = x_test.reshape(len(x_test), 28, 28, 1)

#indicate the model that the features are floating type
features_train = features_train.astype('float')
features_test = features_test.astype('float')

#Normalizee the data for better processing
features_train /= 255
features_test /= 255

#We should convert the target value into hot encoding i.e binary
#since there are 10 classes here so
#for example 2--> 0010000000
#Done by numpy utils

target_train = np_utils.to_categorical(y_train, 10)
target_test = np_utils.to_categorical(y_test, 10)

#Now lets build a CNN model
#we are using Sequential model since the model is to be created in sequenc order followed by filter relu pooling and etc


model = Sequential()
model.add(Conv2D(32, (3,3), input_shape=(28,28,1)))
model.add(Activation('relu'))
model.add(BatchNormalization())

model.add(Conv2D(32, (3,3)))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3)))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64, (3,3)))
model.add(Activation('relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
# flatten at last
model.add(Flatten())
#Now pass create densely connected neural network

model.add(Dense(512))
model.add(BatchNormalization())
#Add dropout

model.add(Dropout(0.2))
#ouptpu leayer
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(features_test, target_test, epochs=10, batch_size=128, verbose=1)

#Test accuracy
score =  model.evaluate(features_test, target_test)
print("Accuracy is = ", score[1])
