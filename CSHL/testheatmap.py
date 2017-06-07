import scipy
import pylab
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import csv
import scipy.spatial.distance as distance

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
data = np.transpose(data)
data = preprocessing.scale(data)

pairwise_dists = distance.squareform(distance.pdist(data,'cityblock'))


# Compute and plot first dendrogram.
fig = pylab.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
Y = sch.linkage(pairwise_dists, method='centroid')
Z1 = sch.dendrogram(Y, orientation='right')
ax1.set_xticks([])
ax1.set_yticks([])

# Compute and plot second dendrogram.
ax2 = fig.add_axes([0.3,0.71,0.6,0.2])
Y = sch.linkage(pairwise_dists, method='centroid')
Z2 = sch.dendrogram(Y, orientation='right')
ax2.set_xticks([])
ax2.set_yticks([])

# Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
idx1 = Z1['leaves']
idx2 = Z2['leaves']
#pairwise_dists = pairwise_dists[idx1,:]
#pairwise_dists = pairwise_dists[:,idx2]
im = axmatrix.matshow(pairwise_dists, aspect='auto', origin='lower', cmap=pylab.cm.RdBu)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
pylab.colorbar(im, cax=axcolor)
fig.show()
fig.savefig('dendrogram.png')