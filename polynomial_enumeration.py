import numpy as np

def polynomial(x, coeff):
    return sum(a * x**i for i, a in enumerate(coeff))

polynomial(1, (2, 4))