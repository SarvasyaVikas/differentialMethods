import math
# Use this to call math expressions in your functions
# Can do math.e, math.sqrt, etc.


def function(x):  # Input your function here
  y = x**2 + math.e**x

  return y  # return the value of the function


def riemannApproximation(i, f, slices, method):
  # i is initial value
  # f is final value
  # slices is number of slices
  # method is Riemann method (0 for left, 1 for right, 2 for midpoint)
  diff = f - i
  section = diff / slices
  lst = []  # compiles x vals to evaluate at
  if method == 0:  # goes based on method
    for j in range(slices):
      val = j + (i * section)
      lst.append(val)
  elif method == 1:
    for j in range(slices):
      val = j + (i * section) + section
      lst.append(val)
  else:
    for j in range(slices):
      val = j + (i + 0.5) * section
      lst.append(val)

  tot = 0
  for k in range(len(lst)):  # evaluates at lst values
    yVal = function(lst[k])
    delta = yVal * section
    tot += delta  # finds total

  tot = round(tot, 3)  # rounds total
  return tot


# Inputs for parameters
i = float(input("What is the first bound? "))
f = float(input("What is the second bound? "))
slices = int(input("How many slices would you like? "))
method = int(input("What method would you like? "))
# Method refers to Riemann method
# 0 for left, 1 for right, 2 for midpoint

print(riemannApproximation(i, f, slices, method))
# Riemann Approximation complete!
