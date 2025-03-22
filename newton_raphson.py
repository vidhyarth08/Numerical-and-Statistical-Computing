def f(x):
    return x**3 - 5

def df(x):
    return 3*x**2

def newton(x):
    while abs(f(x)) > 1e-5:
        x = x - f(x)/df(x)

    return x

print(newton(2))