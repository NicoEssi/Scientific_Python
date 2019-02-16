import numpy as np
import matplotlib.pyplot as plt

def correlated_time_series(T, a):
    y = [a*np.random.randn()]
    for i in range (T):
        e = np.random.randn()
        y.append(e + a*y[i])
    return y

def time_series_array(T, A):
    for a in A:
        y = [a*np.random.randn()]
        for i in range (T):
            e = np.random.randn()
            y.append(e + a*y[i])
        plt.plot(y, label=f"α = {a}")
    plt.legend()
    plt.show()
    
A = [0.0, 0.8, 0.98]
time_series_array(200, A)