import numpy as np

def num_polynomial(x, coeff):
    X_arr = np.empty(len(coeff))
    X_arr[0] = 1
    X_arr[1:] = x
    y = np.cumprod(X_arr)
    return y @ coeff

coef = np.ones(3)
print(coef)
print(num_polynomial(1, coef))