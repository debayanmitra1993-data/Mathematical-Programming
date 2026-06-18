import numpy as np 

class KMeans:
  def __init__(self, k):
    self.k = k
    self.tolerance = 0.0001
    self.max_iter = 10000

  def compute_dist(self, p1, p2):
    return np.sum((p1 - p2)**2)

  def compute_wcss(self):
    wcss_val = 0
    for clusteridx in self.clusters.keys():
      centroid = self.centroids[clusteridx]
      points_cluster = self.X[self.clusters[clusteridx]]
      for point in points_cluster:
        wcss_val += self.compute_dist(centroid, point)
    return wcss_val

  # X -> np.ndarray (n_data x dims)
  def fit(self, X):
    self.X = X
    self.dims = len(X[0])
    self.n_data = len(X)

    # initialize 'k' centroids
    k_indices = np.random.randint(0, self.n_data, self.k)

    # centroids -> (k x dims)
    self.centroids = self.X[k_indices]

    # Loop till convergence
    self.iter_count = 0
    prev_wcss = float("inf")
    while self.iter_count < self.max_iter:
      # assign each point to nearest cluster
      # clusters -> hashmap -> {clusteridx : [rowidx1, rowidx3, .....]}
      self.clusters = {i:[] for i in range(self.k)}
      for rowidx in range(len(self.X)):
        x = self.X[rowidx]
        min_dist = float("inf")
        min_cluster_idx = -1
        for clusteridx in range(len(self.centroids)):
          centroid = self.centroids[clusteridx]
          dist = self.compute_dist(x, centroid)
          if dist < min_dist:
            min_dist = dist
            min_cluster_idx = clusteridx
        self.clusters[min_cluster_idx].append(rowidx)

      # update centroids of each cluster
      for clusteridx in self.clusters.keys():
        points_in_this_cluster = self.X[self.clusters[clusteridx]]
        if len(points_in_this_cluster) > 0:
          self.centroids[clusteridx] = np.mean(points_in_this_cluster, axis = 0)
        else:
          self.centroids[clusteridx] = np.array([np.inf]*self.dims)

      self.iter_count += 1
      # check convergence criteria -> if met, then break
      current_wcss = self.compute_wcss()
      if abs(current_wcss - prev_wcss) < self.tolerance:
        break
      prev_wcss = current_wcss
