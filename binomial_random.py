from numpy.random import uniform

def binomial_array(n,p):
    draw = []
    for i in range(n):
        if uniform() >= p:
            draw.append(1)
        else:
            draw.append(0)
    return draw

binomial_array(10,0.5)