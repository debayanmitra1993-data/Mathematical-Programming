def fx(x):
  return (x**2) - 4

x_l = 1
x_u = 7
ZERO_THRESHOLD = 0.001

while (1):
  x = (x_l + x_u)/2
  if abs(fx(x)) < ZERO_THRESHOLD:
    break
  else:
    if fx(x) > 0:
      x_u = x
    elif fx(x) < 0:
      x_l = x
 
 print('approximate root = ',x) 
