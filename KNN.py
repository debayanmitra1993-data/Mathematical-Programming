import numpy as np 

class KNN:
  def __init__(self, k):
    self.k = k
  
  def fit(self, X, y):
    self.X = X
    self.y = y
  
  def predict(self, X):
    preds = []
    for x_query_idx in range(len(X)):
      x_query = X[x_query_idx]
      preds.append(self.predict_point(x_query))
    return np.array(preds)
  
  def predict_point_fast(self,x_query):
    self.max_heap = []
    for pt_idx in range(len(self.X)):
      x_train_pt = self.X[pt_idx]
      y_train_pt = self.y[pt_idx]

      distval = self.compute_dist(x_query, x_train_pt)
      if len(self.max_heap) < self.k or distval < self.max_heap[0][0]:
        self.push_maxheap([distval, y_train_pt])
    print("max_heap = ", self.max_heap)
    return np.mean([d[1] for d in self.max_heap])
      
  
  def push_maxheap(self, node):
    if len(self.max_heap) < self.k:
      self.max_heap.append(node)
      self.siftUp()
    else:
      self.max_heap.append(node)
      self.max_heap[0], self.max_heap[len(self.max_heap) - 1] = self.max_heap[len(self.max_heap) - 1], self.max_heap[0]
      popped_ele = self.max_heap.pop()
      self.siftDown(0, len(self.max_heap) - 1)
  
  def siftDown(self, idx, endidx):
    c_idx_1 = (2*idx) + 1 
    c_idx_2 = (2*idx) + 2 
    max_idx = idx 
    if c_idx_1 <= endidx:
      if self.max_heap[c_idx_1][0] > self.max_heap[max_idx][0]:
        max_idx = c_idx_1 
    if c_idx_2 <= endidx:
      if self.max_heap[c_idx_2][0] > self.max_heap[max_idx][0]:
        max_idx = c_idx_2 
    if max_idx != idx:
      self.max_heap[idx], self.max_heap[max_idx] = self.max_heap[max_idx], self.max_heap[idx]
      self.siftDown(max_idx, endidx)

  def siftUp(self):
    idx = len(self.max_heap) - 1
    p_idx = (idx - 1) // 2
    while p_idx >= 0:
      if self.max_heap[idx][0] > self.max_heap[p_idx][0]:
        self.max_heap[idx], self.max_heap[p_idx] = self.max_heap[p_idx] , self.max_heap[idx]
        idx = p_idx 
        p_idx = (p_idx - 1) // 2 
      else:
        break 
  
  def predict_point(self, x_query):
    dists = []
    for pt_idx in range(len(self.X)):
      x_train_pt = self.X[pt_idx]
      y_train_pt = self.y[pt_idx]

      distval = self.compute_dist(x_query, x_train_pt)
      dists.append([y_train_pt, distval])
    dists.sort(key = lambda x : x[1])
    return float(np.mean([int(d[0]) for d in dists[:self.k]]))

  def compute_dist(self, x1, x2):
    return float(np.sqrt(np.sum((x1 - x2)**2)))
