from sklearn import cluster
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def cluster_sentences(sentences: list[str], n_clusters=10):
  print("Clustering sentences...")
  print("Length before:", len(sentences))
  vectorizer = TfidfVectorizer()
  encodings = vectorizer.fit_transform(sentences)
  clusters = cluster.KMeans(n_clusters=n_clusters).fit(encodings)
  labels = clusters.labels_

  indices = np.unique([np.where(labels == i)[0][0] for i in range(n_clusters)])
  print("Length after:", len(indices))
  return indices