import numpy as np
from random import uniform

class ECDF:
    def __init__(self, observations):
        self.observations = np.asarray(observations)
    
    def __call__(self, x):
        c = self.observations <= x
        return np.sum(c) / len(self.observations)

samples = [uniform(0, 1) for i in range(100000)]
F = ECDF(samples)

print(F(0.5))  # Evaluating ecdf at x = 0.5