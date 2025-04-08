import numpy as np

def gauss_seidel(A, b, x0=None, tolerance=1e-10, max_iterations=1000):
    if x0 is None:
        x0 = np.zeros_like(b)
        
    x = x0.copy()  
    n = len(b)
    
    for iteration in range(max_iterations):
        x_new = x.copy()
        
        for i in range(n):
            sum_ax = np.dot(A[i], x_new)  
            
            x_new[i] = (b[i] - sum_ax + A[i][i] * x_new[i]) / A[i][i]
        
        if np.linalg.norm(x_new - x) < tolerance:
            print(f"Convergence reached after {iteration+1} iterations.")
            return x_new
        
        x = x_new
    
    print("Maximum iterations reached.")
    return x


if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]], dtype=float)
    b = np.array([15, 10, 10, 10], dtype=float)
    
    solution = gauss_seidel(A, b)
    print("Solution:", solution)