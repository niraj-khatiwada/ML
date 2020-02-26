import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score


datasets = pd.read_csv("C:\\Users\\niraj\\Anaconda3\\Projects\\Logistic Regression\\credit_data.csv")
print(datasets.head())
print(datasets.describe())
print(datasets.corr())

features = datasets[["income", "age", "loan"]]
target = datasets["default"]



features_train, features_test, target_train, target_test = train_test_split(features, target, test_size = 0.3)

model = LogisticRegression()
model.fit(features_train, target_train)
print(model.predict(features_test))
print(model.coef_)


print("Confusion Matrix= ", confusion_matrix(target_test, model.predict(features_test)))
print("Accuracy score = ", accuracy_score(target_test, model.predict(features_test)))