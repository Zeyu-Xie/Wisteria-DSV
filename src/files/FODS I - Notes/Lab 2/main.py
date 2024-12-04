import random
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import pairwise_distances, confusion_matrix
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.datasets import make_blobs

np.random.seed(0)
N_samples = 10000
Centers_Nelliptic_true = np.array([[4,4], [-2,-1], [2,-3], [1,1]])
Stds = np.array([0.4, 0.1, 0.75, 1.2])

# Part 1: Generate the Plot

# X_Nelliptic, y_Nelliptic_true = make_blobs(n_samples=N_samples, centers=Centers_Nelliptic_true, cluster_std=Stds, random_state=0)

transformation = np.array([[0.60834549, -0.63667341], [-0.40887718, 0.85253229]])
X_Elliptic, y_Elliptic_true = make_blobs(
    n_samples=N_samples, 
    centers=Centers_Nelliptic_true, 
    cluster_std=Stds, 
    random_state=0
)
X_Elliptic = np.dot(X_Elliptic, transformation)
Centers_Elliptic_true = np.dot(Centers_Nelliptic_true, transformation)

# Part 2: Draw the Scatter Plot

plt.figure(1)
colors = ["red", "yellow", "blue", "green"]

# for k,col in enumerate(colors):
#     cluster_data = y_Nelliptic_true == k
#     plt.scatter(X_Nelliptic[cluster_data, 0], X_Nelliptic[cluster_data, 1], c=col, marker=".", s=10)
for k, col in enumerate(colors):
    cluster_data = y_Elliptic_true == k
    plt.scatter(X_Elliptic[cluster_data, 0], X_Elliptic[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(Centers_Nelliptic_true[:, 0], Centers_Nelliptic_true[:, 1], c="black", marker="x", s=50)


# plt.title("Scatter Plot of the Random Dataset (Non-Elliptic)")
plt.title("Scatter Plot of the Random Dataset (Elliptic)")
plt.xticks([])
plt.yticks([])
plt.show()