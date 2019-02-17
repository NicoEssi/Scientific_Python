import numpy as np

def bisect_func(f, a, b):
    
    atob = 1/10000
    lower, upper = a, b
    
    if (b - a) < atob:
        val = (b + a)/2
        print(val)
        return val
    else:
        middle = (b + a)/2
        if f(middle) > 0:
            bisect_func(f, lower, middle)
        else:
            bisect_func(f, middle, upper)
            

f = lambda x: np.sin(3*x * (x - 0.37)) + x + x**21 - 1
bisect_func(f, 0, 1)