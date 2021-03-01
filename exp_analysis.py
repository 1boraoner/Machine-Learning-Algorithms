from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

datasize = 1000
(datas, y) = make_blobs(n_samples=datasize,
                        n_features=2, centers=3)
plt.figure(figsize=(10, 10))
plt.scatter(datas[:, 0], datas[:, 1])
plt.show()

# Define number of clusters --> K value
K = 3
# Randomly select K number of data from the dataset as centroids witouht replacement
cents = np.random.randint(low=0, high=datasize, size=(K))
cents = datas[cents]
# print(cents)
# keep iterating until no change in centroids
for iter_num in range(5):

    # compute all data points distances to all centroids
    distances = list([[0], [0], [0]])
    for i, c in enumerate(cents):
        distances[i] = list(map(lambda dist: np.sqrt(
            np.square(c[0]-dist[0])+np.square(c[1]-dist[1])), datas))
    distances = np.array(distances)

    # group the data points around the centroids
    clusters = list([[], [], []])
    for ind, point in enumerate(distances.transpose()):
        clusters[np.where(min(point) == point)[0][0]].append(ind)

    # assign new centroids
    means = list()
    for i in range(K):
        means.append(np.mean(datas[clusters[i]], axis=0))
    cents = means

# predicted y categories
y_pred = np.zeros(shape=(datasize))
# due to categorization is made by the make_blob function to be on the same 0,1,2 values=> single data representation is looked up
y_pred[clusters[0]] = y[clusters[0][0]]
y_pred[clusters[1]] = y[clusters[1][0]]
y_pred[clusters[2]] = y[clusters[2][0]]

# scatter plot
plt.figure(figsize=(10, 10))
plt.scatter(datas[:, 0], datas[:, 1], c=y_pred)
plt.show()


# evalutaion of the algorithm
print(classification_report(y, y_pred))
print(confusion_matrix(y, y_pred))
