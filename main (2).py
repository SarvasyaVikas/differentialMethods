stepSize = float(input("What do you want as the step size? "))
steps = int(input("How many steps do you want to take? "))
initialX = float(input("What is the initial x value? "))
initialY = float(input("What is the initial y value? "))

def differentialEquation(x, y): # Input your function here
  dydx = x ** 2
  # Change this function to your function

  return dydx

yNew = [initialY]
xNew = [initialX]

for i in range(steps):
   delta = differentialEquation(xNew[-1], yNew[-1]) * stepSize
   newVal = yNew[-1] + delta
   newX = xNew[-1] + stepSize
   xNew.append(newX)
   yNew.append(newVal)

print(yNew[-1])