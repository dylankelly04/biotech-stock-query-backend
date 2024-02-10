from sentence_transformers import SentenceTransformer, util
from sklearn import cluster
import numpy as np


def cluster_sentences(sentences: list[str], n_clusters=10):
  print("Clustering sentences...")
  print("Length before:", len(sentences))
  model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
  encodings = [model.encode(s, convert_to_numpy=True) for s in sentences]

  points = np.array(encodings)
  clusters = cluster.KMeans(n_clusters=n_clusters).fit(points)
  labels = clusters.labels_

  indices = np.unique([np.where(labels == i)[0][0] for i in range(n_clusters)])
  print("Length after:", len(indices))
  return indices