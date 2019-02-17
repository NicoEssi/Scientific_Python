import numpy as np
from random import uniform

class discreteRV:
    
    def __init__(self, q):
        self.q = q
        self.Q = np.cumsum(q)
        
    def draw(self, k = 1):
        return self.Q.searchsorted(uniform(0, 1, size = k))


def sample(q):
    a = 0.0
    U = uniform(0, 1)
    for i in range(len(q)):
        if a < U <= a + q[i]:
            return i, U
        a = a + q[i]
       
q = [0.25, 0.75]
sample(q)

q = (0.1, 0.9)
d = discreteRV(q)