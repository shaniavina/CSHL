from sklearn.cluster import AgglomerativeClustering
import numpy as np
from sklearn import preprocessing
import scipy 
import pylab
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram, linkage
import csv
import scipy.spatial.distance as distance
from sklearn.cluster import k_means

data = []

numOfSample = 20000
with open('sp3combined.test.txt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == "RowNames":
            continue
        if len(data) == numOfSample:
            break
        data.append(row[4:])

data = np.array(data)
data = data.astype(np.float)

data = preprocessing.scale(data)

centroid, label, inertia = k_means(X = data, n_clusters = 2, init='k-means++', precompute_distances=True, n_init=10)

print(np.sum(label))
import csv
with open("centroid.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(centroid)

labelV = [[l] for l in label]
with open("label.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(labelV)

'''
fig = pylab.figure(figsize=(100,100))
pairwise_dists = distance.squareform(distance.pdist(data))
clusters = sch.linkage(pairwise_dists, method='complete')
den = sch.dendrogram(clusters, color_threshold=np.inf, no_plot=False)
fig.show()
fig.savefig('dendrogram.png')
D = scipy.zeros([numOfSample, numOfSample])
for i in range(numOfSample):
    for j in range(numOfSample):
        dis = data[i] - data[j]
        D[i, j] = np.linalg.norm(dis)
        
fig = pylab.figure(figsize=(8,8))
ax1 = fig.add_axes([0.1,0.1,0.5,0.5])
Y = sch.linkage(D, method='centroid')
Z1 = sch.dendrogram(Y, orientation='right')
ax1.set_xticks([])
ax1.set_yticks([])
fig.show()
fig.savefig('dendrogram.png')
'''
