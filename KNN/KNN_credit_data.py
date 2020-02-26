import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import cross_val_score

datasets = pd.read_csv("C:\\Users\\niraj\\Anaconda3\\Projects\\KNN\\credit_data.csv")
features = datasets[["income", "age", "loan"]]
target = datasets["default"]

features = preprocessing.MinMaxScaler().fit_transform(features)
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3)


cross_validation = []
for i in range(1, 100):
    knn = KNeighborsClassifier(n_neighbors=i)
    score = cross_val_score(knn, features, target, cv= 10) # no need to define scoring
    cross_validation.append(score.mean())


index = np.argmax(cross_validation)
print(index)
print(cross_validation)

classifier = KNeighborsClassifier(n_neighbors=32) #k obtained from cross validation
classifier.fit(features_train, target_train)

# prec = classifier.predict(features_test)

print("Confusion Matrix: ", confusion_matrix(target_test, classifier.predict(features_test)))
print("Accuracy score is: ", accuracy_score(target_test, classifier.predict(features_test)))