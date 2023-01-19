def equation(x):  # Type in your equation here
  y = x**2

  return y  # Returns value


def descent(xI, increment, y):  # Descending the function (for min)
  xF = xI + increment  # Finding the increment
  diff = equation(xF) - equation(xI)
  delta = diff * increment  # Finding the change in y
  if delta > 0:  # Descending the derivative
    yF = y - delta
    x = xI - increment
    return (x, yF, False)
  elif delta < 0:
    yF = y + delta
    return (xF, yF, False)
  else:  # Function over
    xC = (xF + xI) / 2
    yC = equation(xC)
    return (xC, yC, True)


def ascent(xI, increment, y):  # Same function but for max
  xF = xI + increment
  diff = equation(xF) - equation(xI)
  delta = diff * increment
  if delta > 0:  # Ascending the derivative
    yF = y + delta
    return (xF, yF, False)
  elif delta < 0:
    yF = y - delta
    x = xI - increment
    return (x, yF, False)
  else:
    xC = (xF + xI) / 2
    yC = equation(xC)
    return (xC, yC, True)


# Inputs for parameters
# Choose these carefully to get a good value
xStart = float(input("Initial x Value: "))
yStart = float(input("Initial y Value: "))
increment = float(input("Descent Rate: "))
threshold = float(input("Threshold: "))
minmax = int(input("Minimum (0) or Maximum (1)? "))
sims = int(input("Number of Simulations: "))

xVals = [xStart]  # Stores generated values
yVals = [yStart]

if minmax == 0:  # Mins
  for i in range(sims):
    (xNew, yNew, tf) = descent(xVals[-1], increment, yVals[-1])
    xVals.append(xNew)
    yVals.append(yNew)
    if tf == True or abs(yVals[-1] - yVals[-2]) < threshold:
      print("Minimum point is found at ({}, {})".format(xVals[-1], yVals[-1]))
      break

    if i == 999:
      print("Minimum was not found. The equation is likely unbounded.")
else:  # Maxes
  for i in range(sims):
    (xNew, yNew, tf) = ascent(xVals[-1], increment, yVals[-1])
    xVals.append(xNew)
    yVals.append(yNew)
    if tf == True or abs(yVals[-1] - yVals[-2]) < threshold:
      print("Maximum point is found at ({}, {})".format(xVals[-1], yVals[-1]))
      break

    if i == 999:
      print("Maximum was not found. The equation is likely unbounded.")

# Critical Point Locator