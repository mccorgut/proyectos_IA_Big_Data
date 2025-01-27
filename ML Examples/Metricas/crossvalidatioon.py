from sklearn import datasets
from sklearn import svm

X, y = datasets.load_iris(return_X_y=True)

from sklearn.model_selection import cross_val_score

clf = svm.SVC(kernel='linear', C=1, random_state=42)
scores = cross_val_score(clf, X, y, cv=5)
print(scores)
