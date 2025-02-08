#Regula Falsi method to find the roots of non-linear equations. It is an another method besides Bisection method.
#It is also known as False Position method.
import math as m

def f(x):
    return x * m.log(x) - 1.2

def regula_falsi(x0,x1,eps=1e-5):
    if f(x0) * f(x1) <= 0:
        print("f(x0) and f(x1) should have opposite signs.")
        return None
    
    for i in range(4):
        x = x0 - ((x1 - x0) / (f(x1) - f(x0))) * f(x0)

        if abs(f(x)) < eps:
            print(f"Root is: {x:.6f}")
            return x
        
        if f(x) * f(x0) > 0:
            x1 = x
        else:
            x0 = x

    print("No root is found.")
    return None

x0 = 2
x1 = 3
root = regula_falsi(x0,x1)
