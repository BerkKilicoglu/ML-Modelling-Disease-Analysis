import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from functions import *
from sklearn.decomposition import PCA
from sklearn.metrics import v_measure_score
from sklearn.preprocessing import LabelEncoder

path = os.path.join('dataset','diabetes_health_indicators.xlsx')
df = pd.read_excel(path)
le = LabelEncoder()
df['Diabetes_binary'] = le.fit_transform(df['Diabetes_binary'])
y = df['Diabetes_binary']
del df['Diabetes_binary']


pca = PCA(n_components=2)
pca.fit(df)

df_reduced = pca.transform(df)

kmeans = KMeans( init = 'random', n_clusters = 4 , n_init = 10)

kmeans.fit(df)

clusters = kmeans.predict(df)

df_clustered = pd.DataFrame(df, columns = df.columns, index= df.index)
df_clustered['cluster'] = clusters


df_reduceddf = pd.DataFrame(df_reduced, index = df.index, columns=['PC1', 'PC2'])
df_reduceddf['cluster'] = clusters

#centres_reduced = pca.transform(kmeans.cluster_centers_)

display_factorial_planes(df_reduced, 2, pca, [(0,1)], illustrative_var = clusters, alpha = 0.5)

#plt.scatter(centres_reduced[:,0], centres_reduced[:,1],
 #           marker='x', s=169, linewidths=3,
 #           color = 'r', zorder = 10) 
          
v_scores = []

v_scores.append(v_measure_score(y, clusters))
print(v_scores)
