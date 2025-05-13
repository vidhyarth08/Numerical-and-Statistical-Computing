def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if f_x1 - f_x0 == 0:
            print("Zero division error in iteration", i)
            return None
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        
        if abs(x2 - x1) < tol:
            return x2
        
        x0, x1 = x1, x2
    
    print("Did not converge within the maximum number of iterations.")
    return None

def f(x):
    return x**3 - x - 2

x0 = 1
x1 = 2

root = secant_method(f, x0, x1)

print(f"Root: {root}")