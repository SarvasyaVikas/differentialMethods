# Provides exact, accurate values of integration (not an approximation)


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


def integration(x, s, e):  # repetitively performs inversePowerRule on terms
  terms = function(x)
  length = len(terms) // 3  # finds number of three-sequences
  initial = 0
  final = 0
  for i in range(length):
    term = [terms[3 * i], terms[3 * i + 1], terms[3 * i + 2]]
    # finds smaller term
    (c, v, p) = inversePowerRule(term)

    iVal = (s**p) * c  # calculates first bound value
    fVal = (e**p) * c  # calculates second bound value
    initial += iVal  # adds it to first bound total
    final += fVal  # adds it to second bound total

  integrated = final - initial  # finds definite integral
  integrated = round(integrated, 3)

  return integrated  # returns the integrated polynomial


print(integration('x', 1, 4))
# Definite Integration complete!
