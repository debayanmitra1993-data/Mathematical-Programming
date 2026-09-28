class MaxHeap:
  def __init__(self, array):
    self.max_heap = self.build_max_heap(array)
  
  def peek(self):
    if len(self.max_heap) == 0:
      return "Max Heap Empty"
    return self.max_heap[0]
  
  def push(self, ele):
    self.max_heap.append(ele)
    self.siftUp(len(self.max_heap) - 1)
  
  def siftUp(self, idx):
    p_idx = (idx - 1) // 2
    while p_idx >= 0:
      if self.max_heap[idx] > self.max_heap[p_idx]:
        self.max_heap[idx], self.max_heap[p_idx] = self.max_heap[p_idx], self.max_heap[idx]
        idx = p_idx
        p_idx = (p_idx - 1) // 2
      else:
        break
  
  def pop(self):
    if len(self.max_heap) == 0:
      return "Max Heap Empty"
    self.max_heap[0], self.max_heap[len(self.max_heap) - 1] = self.max_heap[len(self.max_heap) - 1], self.max_heap[0]
    catch_ele = self.max_heap.pop()
    self.siftDown(0, self.max_heap, len(self.max_heap) - 1) 
    return catch_ele
  
  def build_max_heap(self, array):
    last_internal_idx = (len(array) // 2) - 1
    for idx in range(last_internal_idx, -1, -1):
      self.siftDown(idx, array, len(array) - 1)
    return array
  
  def siftDown(self, idx, array, endidx):
    c_idx_1 = (2*idx) + 1
    c_idx_2 = (2*idx) + 2
    max_idx = idx
    if c_idx_1 <= endidx:
      if array[c_idx_1] > array[max_idx]:
        max_idx = c_idx_1
    if c_idx_2 <= endidx:
      if array[c_idx_2] > array[max_idx]:
        max_idx = c_idx_2
    if max_idx != idx:
      array[idx], array[max_idx] = array[max_idx], array[idx]
      self.siftDown(max_idx, array, endidx)
