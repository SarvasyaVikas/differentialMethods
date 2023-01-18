def de(x, y): # Input your differential equation here
  dydx = x**3

  return dydx # Calculates the differential


def rk4(fn, xI, xF, yI):
  k1 = de(xI, yI) # Finds k1 using the initial values
  h = xF - xI # interval
  section = h / 2.0 # section increment

  deltaK2 = k1 * section # Finds new approximated x, y
  xM = xI + section
  yK2 = yI + deltaK2
  k2 = de(xM, yK2) # Finds k2

  deltaK3 = k2 * section # Finds new approximated x, y
  yK3 = yI + deltaK3
  k3 = de(xM, yK3) # Finds k3

  deltaK4 = k3 * h # Finds new x, y
  yK4 = yI + deltaK4
  k4 = de(xF, yK4) # Finds k4

  weightedK1 = k1 / 6
  weightedK2 = k2 / 3
  weightedK3 = k3 / 3
  weightedK4 = k4 / 6

  deltaF = (weightedK1 + weightedK2 + weightedK3 + weightedK4) * h # weighted average of slopes
  yF = yI + deltaF # Final y value

  return yF

# Inputs to determine parameters
steps = int(input("Number of Steps: "))
stepSize = float(input("Step Size: "))
xStart = float(input("Initial x Value: "))
yStart = float(input("Initial y Value: "))

yVals = [yStart]

# Runs RK4 for each step
for i in range(steps):
  xI = i * stepSize + xStart
  xF = xI + stepSize
  yI = yVals[-1]
  yF = rk4(de, xI, xF, yI)
  yVals.append(yF)

 # Returns the final value
print(yVals[-1])

# As a side note, since this is RK4, all functions with an integral of degree 4 or lower will be given exact values
# For example, x^3 or x^2 will be perfectly accurate. However, x^4, x^5, or more will be approximations
