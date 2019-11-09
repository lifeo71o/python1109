
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()
print(list(iris.keys()))

X = iris["data"][:, 3:]
y = (iris["target"]==2).astype(np.int)
print(X) # breakpoint here
