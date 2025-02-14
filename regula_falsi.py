#Regula Falsi method to find the roots of non-linear equations. It is an another method besides Bisection method.
#It is also known as False Position method.
import math as m

def f(x):
    return x * m.log(x) - 1.2

def regula_falsi(x0,x1,eps=1e-5):
    if f(x0) * f(x1) >= 0:
        print("Regula Falsi method fails.")
        return None
    
    for _ in range(100):
        x = x0 - (f(x0) * (x1 - x0) / (f(x1) - f(x0)))

        if abs(f(x)) < eps:
            print(f"Root is: {x}")
            return x
        
        if f(x0) * f(x) < 0:
            x1 = x
        else:
            x0 = x

    return None

x0 = 2
x1 = 3
root = regula_falsi(x0,x1)
