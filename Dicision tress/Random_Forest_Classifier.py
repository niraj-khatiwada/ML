from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_predict

dataset = load_iris()

features = dataset['data']
target = dataset['target']

features = MinMaxScaler().fit_transform(features)
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2)

model = RandomForestClassifier()
fittedmodel = model.fit(features_train, target_train)
prediciton = model.predict(features_test)

# print("predicition is=", prediciton)
print("Confusion matrix is= ", confusion_matrix(target_test, prediciton))
print("Accuracy score is= ", accuracy_score(target_test, prediciton))
print("------After cross validating---------")
cross_validated_score =  cross_val_predict(model, features, target, cv=10)
print("Accuracy is= ", accuracy_score(target, cross_validated_score))