from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np

X = np.r_[np.random.randn(50, 2) + [2, 2],
          np.random.randn(50, 2) + [0, -2],
          np.random.randn(50, 2) + [-2, 2]
]
print(X.shape, X[:10])
for element in X:
    plt.scatter(element[0], element[1], c='black', s=7)

plt.show()
print("min,max", np.min(X), np.max(X))
print("min, max with row,", np.min(X, axis=0), np.max(X, axis=0))
k = 3
C_x = np.random.uniform(np.min(X, axis=0)[0], np.max(X, axis=0)[0], size=k)
C_y = np.random.uniform(np.min(X, axis=0)[1], np.max(X, axis=0)[1], size=k)
#C_x = np.random.randint(np.min(X, axis=0)[0], np.max(X, axis=0)[0], size=k)
#C_y = np.random.randint(np.min(X, axis=0)[1], np.max(X, axis=0)[1], size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
plt.scatter(C_x, C_y, marker='*', s=200, c='#40FFEE')
plt.show()