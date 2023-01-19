def inversePowerRule(term):  # Performs inverse power rule on a 'term'
  newPower = term[2] + 1  # the term is a list of three values
  newCoeff = term[0] / newPower
  return (newCoeff, term[1], newPower)


def function(x):
  terms = [1, x, 2, 4, x, 1, 4, x, 0]
  # first term is the coefficient
  # the second term is the variable (string of letter)
  # the third term is the power or exponent
  return terms


def integration(x):  # repetitively performs inversePowerRule on terms
  terms = function(x)
  length = len(terms) // 3  # finds number of three-sequences
  integrated = []
  for i in range(length):
    term = [terms[3 * i], terms[3 * i + 1], terms[3 * i + 2]]
    # finds smaller term
    (c, v, p) = inversePowerRule(term)
    c = round(c, 2)  # rounds values
    p = round(p, 2)
    if c > 0:  # adds + or -
      string = "+{}{}^{}".format(c, v, p)
      integrated.append(string)
    else:
      string = "{}{}^{}".format(c, v, p)
      integrated.append(string)

  integrated = "".join(integrated)  # makes the terms a string together

  return integrated  # returns the integrated polynomial


print(integration('x'))
# Indefinite Integration complete!
