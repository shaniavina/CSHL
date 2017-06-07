import numpy as np
from sklearn import preprocessing
import scipy 
import pylab
from scipy.cluster.hierarchy import dendrogram, linkage
import csv
import scipy.spatial.distance as distance
from sklearn.cluster import k_means
import matplotlib.pyplot as plt
from matplotlib import gridspec

data = []

chromes = []
chrome = []
count = 0
currentChrome = None
numOfSample = 20000
with open('sp3combined.test.txt') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == "RowNames":
            continue
        if len(data) == numOfSample:
            break
        data.append(row[4:])
        if currentChrome and int(row[1]) != currentChrome:
            chromes.append(np.array(chrome))
            chrome = []
        chrome.append(int(row[1]))
        currentChrome = int(row[1])
chromes.append(np.array(chrome))

for c in chromes:
    print(len(c), c)

data = np.array(data)
data = data.astype(np.float)

data = preprocessing.scale(data)

data = np.transpose(data)


##############
fig = plt.figure(figsize=(250, 250))
pairwise_dists = distance.squareform(distance.pdist(data,'cityblock'))
clusters = linkage(pairwise_dists, method='complete')
 
with open("clusters_1.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(clusters)
 
labels = ["CTB11126.DCIS","CTB11127.DCIS","CTB11128.DCIS","CTB11129.DCIS","CTB11130.DCIS","CTB11131.DCIS","CTB11132.DCIS","CTB11133.DCIS","CTB11134.DCIS","CTB11135.DCIS","CTB11136.DCIS","CTB11137.DCIS","CTB11138.DCIS","CTB11139.DCIS","CTB11140.DCIS","CTB11141.DCIS","CTB11142.DCIS","CTB11143.DCIS","CTB11144.DCIS","CTB11145.DCIS","CTB11146.DCIS","CTB11147.DCIS","CTB11148.DCIS","CTB11149.DCIS","CTB11150.DCIS","CTB11151.DCIS","CTB11152.DCIS","CTB11153.DCIS","CTB11154.DCIS","CTB11155.DCIS","CTB11156.DCIS","CTB11157.DCIS","CTB11158.DCIS","CTB11159.DCIS","CTB11160.DCIS","CTB11161.DCIS","CTB11162.DCIS","CTB11163.DCIS","CTB11164.DCIS","CTB11165.DCIS","CTB11166.DCIS","CTB11167.DCIS","CTB11168.DCIS","CTB11169.DCIS","CTB11170.DCIS","CTB11171.DCIS","CTB11172.DCIS","CTB11173.DCIS","CTB11174","CTB11175","CTB11176","CTB11177","CTB11178","CTB11179","CTB11180","CTB11181","CTB11182","CTB11183","CTB11184","CTB11185","CTB11186","CTB11187","CTB11188","CTB11189","CTB11190","CTB11191","CTB11192","CTB11193","CTB11194","CTB11195","CTB11196","CTB11197","CTB11199","CTB11200","CTB11201","CTB11202","CTB11203","CTB11204","CTB11205","CTB11206","CTB11207","CTB11208","CTB11209","CTB11210","CTB11211","CTB11212","CTB11213","CTB11214","CTB11215","CTB11216","CTB11217","CTB11218","CTB11219","CTB11220","CTB11221"]
 
den = dendrogram(clusters, color_threshold=np.inf, no_plot=False, labels = labels, leaf_font_size = 10)
 
fig.show()
# fig.savefig("den.png")
###################

fig = plt.figure(figsize=(len(chromes) * 30, 250))

hr = [2] + [1 for i in range(len(chromes))]

gs = gridspec.GridSpec(len(chromes) + 1, 1, width_ratios=[1], height_ratios = hr)

lvs = scipy.zeros([1, len(den["ivl"])])
count = 0
for l in den["ivl"]:
    if l.find("DCIS") == -1:
        lvs[0][count] = 0
    else:
        lvs[0][count] = 1
    count += 1

#####################


bar = fig.add_subplot(gs[0])
bar.matshow(lvs, aspect='auto', origin='lower', cmap=pylab.cm.Greens)
bar.set_xticklabels([])
bar.set_yticklabels([])
bar.set_yticks([])
bar.set_xticks([])


#############

data = np.transpose(data)
data = data[:, den["leaves"]]

# Three states
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i][j] < 0.9:
            data[i][j] = 0
        elif data[i][j] < 1.1:
            data[i][j] = 1
        else:
            data[i][j] = 2

count = 2
for c in chromes:
    label = str(count - 1)
    varis = fig.add_subplot(gs[count - 1])
    varis.matshow(data[c], aspect='auto', cmap=pylab.cm.RdBu)
    varis.set_ylabel(label)
    varis.set_xticklabels([])
    varis.set_yticklabels([])
    varis.set_yticks([])
    varis.set_xticks([])
    count += 1

fig.show()
fig.savefig("varis.png")

