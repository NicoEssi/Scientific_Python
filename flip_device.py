import numpy as np
from numpy.random import uniform

def flipdevice():
    x = 0
    s = 0
    a = []
    for i in range (10):
        if uniform() >= 0.5:
            x += 1
            a.append(1)
        else:
            x = 0
            a.append(0)
        if x == 3:
            s += 1
            x = 0
    return s, a

flipdevice()