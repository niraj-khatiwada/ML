from sklearn.feature_extraction.text import TfidfVectorizer

list = ["I like machine learning and clustering algorithm",
        "Apples, oranges and any kind of fruit is halthy",
        "Is it feasible iwth machine learning algorith?",
        "My family is happy beachase of healthy fruits"]

ins = TfidfVectorizer()
tfid = ins.fit_transform(list)

print((tfid*tfid.T).A)