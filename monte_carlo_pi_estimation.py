import numpy as np
from numpy.random import uniform

def monte_carlo_pi(n):
    p = 0
    for i in range (n):
        u, v = uniform(), uniform()
        if np.sqrt((u - 0.5)**2 + (v - 0.5)**2) <= 0.5:
            p += 1
    return (p/n)*4

monte_carlo_pi(100000)