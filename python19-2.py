import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans

X = np.r_[np.random.randn(50, 2) + [2, 2],
          np.random.randn(50, 2) + [0, -2],
          np.random.randn(50, 2) + [-2, 2]]
print(X.shape)
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)
print(kmeans.inertia_)

colors = ['c', 'm', 'y', 'k']
markers = ['d', '*', '.', 'o']
for i in range(4):
    dataX = X[kmeans.labels_ == i]
    plt.scatter(dataX[:,0], dataX[:,1],c=colors[i], marker=markers[i])
    print(dataX.size)
plt.show()