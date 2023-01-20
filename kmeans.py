import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

wind_data = pd.read_csv('kmeans_poc.csv')

kmeans = KMeans(n_clusters=5)
kmeans.fit(wind_data)

labels = kmeans.labels_

print(labels)

# Plot the wind data points with different colors for each cluster
for i in range(len(wind_data)):
    if labels[i] == 0:
        plt.scatter(wind_data['tr_median'].loc[i], wind_data['median'].loc[i], c='r', marker='o')
    elif labels[i] == 1:
        plt.scatter(wind_data['tr_median'].loc[i], wind_data['median'].loc[i], c='b', marker='v')
    elif labels[i] == 2:
        plt.scatter(wind_data['tr_median'].loc[i], wind_data['median'].loc[i], c='y', marker='s')
    elif labels[i] == 3:
        plt.scatter(wind_data['tr_median'].loc[i], wind_data['median'].loc[i], c='g', marker='P')      
    else:
        plt.scatter(wind_data['tr_median'].loc[i], wind_data['median'].loc[i], c='pink', marker='D')


# Plot the cluster centroids
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', c='black', s=100)

plt.show()

