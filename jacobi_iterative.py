def jacobi(a, b, x0=None, tol=1e-10, max_iterations=100):
    n = len(b)
    x = x0 if x0 is not None else [0.0 for _ in range(n)]

    for itr in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s = sum(a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / a[i][i]

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new

    raise ValueError("Jacobi method did not converge within the maximum number of iterations.")

a = [[10, 1, 2],
     [1, 10, 1],
     [2, -1, 10, -1],
     [2, 1, 10]]
b = [27, -11, 17]

solution = jacobi(a, b)
print("Solution:", solution)
