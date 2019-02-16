def riemann(f, a, b, n):
    if (a < b) == False:
        print("a < b is not satisfied")
        return
    
    s = 0
    leng = b - a
    step = leng/n
    i = a
    
    while i <= b:
        s += f(i)*step
        i += step
        
    return s


def sqrd(x):
    return x*x


def tripsqrd(x):
    return x*x*x


def weirdf(x):
    return (2*x**3 + x**2 + x/3 + 10)



print(riemann(sqrd, 1, 9, 1000))

print(riemann(tripsqrd, 3, 6, 10000))

print(riemann(weirdf, 2, 7, 100000))