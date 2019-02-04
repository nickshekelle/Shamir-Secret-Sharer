from fractions import Fraction
import random


def eval_polynomial(P, x):
    result = 0
    for coeff in P:
        result = x * result + coeff
    return result


def split(val, n, k):
    # Obtain k-1 random numbers
    klist = []
    for i in range(k-1):
        klist.append(random.randint(1, 1000))
    # Polynomial becomes f(x) = val + (k1)x + ... + (k-1)x^(k-1)
    klist.append(val)
    # for i=1 to n, add (i, f(i) to list
    retlist = []
    for x in range(n):
        retlist.append((x+1, eval_polynomial(klist, x+1)))
    # return list
    return retlist


# points is a list of shares.
# x is the x-coordinate in which to compute the secret at.
# Return the computed secret value.
def interpolate(points, x):
    if len(points) < 2:
        raise ValueError("need at least two points")
    x = []
    y = []
    # split points into x and y
    for m, n in points:
        x.append(m)
        y.append(n)
    # extract lagrange basis least significant coefficient
    lagbasis = [1] * len(x)
    for i in range(0, len(x)):
        for j in range(0, len(x)):
            if j != i:
                lagbasis[i] *= Fraction(-x[j], x[i] - x[j])
    secret = 0
    for q in range(0, len(y)):
        secret += y[q]*lagbasis[q]
    return secret



