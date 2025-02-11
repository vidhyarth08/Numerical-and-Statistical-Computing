#Another method to solve non-linear equations.
import math as m

def f(x):
    return x**3 - x - 11

def bisection(x,y,iter=100,eps=1e-8):
    if f(x)*f(y) >= 0:
        print('Bisection method fails.')
        return None
    
    if f(x)*f(y) < 0:
        for _ in range(iter):
            ans = (x+y)/2
            if abs(f(ans)) < eps or (y-x)/2 < eps:
                print(f'Root is: {ans}')
                return ans
            
            if f(x)*f(ans) < 0:
                y = ans
            else:
                x = ans
    
    print('No root is found.')
    return None

x = 2
y = 3
root = bisection(x,y)