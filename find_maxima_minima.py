import math

def fx(x):
  return (x**2) + math.sin(x) + 2*x

def derivativefx(x):
  return (2*x) + math.cos(x) + 2

def secondderivativefx(x):
  return 2 - math.sin(x)

x_lower = -2
x_upper = 2
EPS = 0.001

while (1):
  x = (x_lower + x_upper)/2
  if abs(derivativefx(x)) < EPS:
    break
  else:
    if derivativefx(x) < 0:
      x_lower = x
    elif derivativefx(x) > 0:
      x_upper = x

print('x, f(x), derivative = ',x, fx(x), derivativefx(x))
if secondderivativefx(x) > 0:
    print('MINIMA obtained , (x,f(x)) = ',x,fx(x))
else:
    print('MAXIMA obtained , (x,f(x)) = ',x,fx(x))
