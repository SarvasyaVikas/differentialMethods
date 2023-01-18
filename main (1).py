def de(x, y):  # input your differential equation here
  dydx = x * y

  return dydx


def rk2(fn, xI, xF, yI):
  k1 = fn(xI, yI)
  h = xF - xI
  deltaM = k1 * h / 2.0
  xM = xI + (h / 2.0)
  yM = yI + deltaM

  k2 = fn(xM, yM)
  deltaF = k2 * h
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
  yF = rk2(de, xI, xF, yI)
  yVals.append(yF)

print(yVals[-1])
