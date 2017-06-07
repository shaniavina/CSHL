from sklearn.cluster import AgglomerativeClustering
import numpy as np

data = np.loadtxt(r'sp3combined.test.txt', delimiter=',', skiprows=19995, usecols=(4,5,6,7,8,9,10))

for d in data:
    estimator = AgglomerativeClustering(n_clusters = 2)
    estimator.fit_predict(d)
    estimator.get_params(d)
