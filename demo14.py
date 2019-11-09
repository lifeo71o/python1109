from sklearn import datasets, svm, model_selection

iris = datasets.load_iris()
svc = svm.SVC()
scores = model_selection.cross_val_score(svc, iris.data, iris.target, cv=10)

print(scores)
print("accuracy:", scores.mean())