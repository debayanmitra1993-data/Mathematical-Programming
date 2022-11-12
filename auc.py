def fx(x):
  return x**3

def auc(x_lower, x_upper, N = 1000):
  area = 0
  delta = (x_upper - x_lower)/N
  
  for idx in range(N):
    x1 = x_lower + ((idx)*delta)
    x2 = x1 + delta
    area += ((delta)*(fx(x1) + fx(x2)))/2
  return area
