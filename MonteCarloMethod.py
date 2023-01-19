import math
# Imports math expressions for use in the function below
# Can be used for math.e, math.sqrt, etc.

import random
# Used for generating points in the monte-carlo method

def function(x): # Type in your function here
  y = x ** 2 + math.e ** x

  return y # returns value of the function

def montecarlo(i, f, p): # montecarlo method
  tot = 0
  for j in range(p): # runs through all the points
    xVal = random.uniform(i, f) # randomly generates them
    yVal = function(xVal) # finds values
    tot += yVal # updates total

  section = (f - i) / p # scales values
  integral = tot * section

  return integral

# Inputs as parameters
i = float(input("Initial Bound: "))
f = float(input("Final Bound: "))
p = int(input("How many points would you like to generate? "))
# Higher number of points gives more accuracy

print(montecarlo(i, f, p))