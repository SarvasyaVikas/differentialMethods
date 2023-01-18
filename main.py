def de(x, y):
  dydx = x**3

  return dydx


def rk4(fn, xI, xF, yI):
  k1 = de(xI, yI)
  h = xF - xI
  section = h / 2.0

  deltaK2 = k1 * section
  xM = xI + section
  yK2 = yI + deltaK2
  k2 = de(xM, yK2)

  deltaK3 = k2 * section
  yK3 = yI + deltaK3
  k3 = de(xM, yK3)

  deltaK4 = k3 * h
  yK4 = yI + deltaK4

  k4 = de(xF, yK4)

  weightedK1 = k1 / 6
  weightedK2 = k2 / 3
  weightedK3 = k3 / 3
  weightedK4 = k4 / 6

  deltaF = (weightedK1 + weightedK2 + weightedK3 + weightedK4) * h
  yF = yI + deltaF

  return yF


steps = int(input("Number of Steps: "))
stepSize = float(input("Step Size: "))
xStart = float(input("Initial x Value: "))
yStart = float(input("Initial y Value: "))

yVals = [yStart]

for i in range(steps):
  xI = i * stepSize + xStart
  xF = xI + stepSize
  yI = yVals[-1]
  yF = rk4(de, xI, xF, yI)
  yVals.append(yF)

print(yVals[-1])
