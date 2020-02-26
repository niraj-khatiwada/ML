import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

datasets = pd.read_csv("C:\\Users\\niraj\\Anaconda3\\Projects\\KNN\\credit_data.csv")
features = datasets[['income', 'age', 'loan']]
target = datasets['default']

features = preprocessing.MinMaxScaler().fit_transform(features)
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3)

model = GaussianNB()
model.fit(features_train, target_train)

print("Predicted value is= ", model.predict(features_test))

print("Confusion matrix is= ", confusion_matrix(target_test, model.predict(features_test)))
print("Accuracy score is= ", accuracy_score(target_test, model.predict(features_test)))


''' Accuracy score

Logistic Regression = 93%
KNN = 98%
NB = 93%
'''