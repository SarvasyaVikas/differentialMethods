def de(x, y):  # input your differential equation here
  dydx = x

  return dydx # Calculate the differential


def rk2(fn, xI, xF, yI): 
  k1 = fn(xI, yI) # Initial differential
  h = xF - xI # interval
  deltaM = k1 * h / 2.0 # finding middle approximation y value
  xM = xI + (h / 2.0)
  yM = yI + deltaM

  k2 = fn(xM, yM) # Updated differential
  deltaF = k2 * h
  yF = yI + deltaF # Final y using updated differential

  return yF

# Inputs to determine parameters
steps = int(input("Number of Steps: "))
stepSize = float(input("Step Size: "))
xStart = float(input("Initial x Value: "))
yStart = float(input("Initial y Value: "))

yVals = [yStart]

# Runs RK2 for each step
for i in range(steps):
  xI = i * stepSize + xStart
  xF = xI + stepSize
  yI = yVals[-1]
  yF = rk2(de, xI, xF, yI)
  yVals.append(yF)

# Prints final value of the function
print(yVals[-1])

# As a side note, RK2 will be perfectly accurate for any function with degree 2 or lower for its integral, like x.
# It will be an approximation for functions like x^2 or x^3
# To use a more accurate method, look at RK4
