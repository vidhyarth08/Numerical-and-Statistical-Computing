def gauss_elimination(a,b):
    n = len(b)
    
    for i in range(n):
        max_row = i + max(range(n - i), key=lambda k: abs(a[i + k][i]))
        if max_row != i:
            a[i], a[max_row] = a[max_row], a[i]
            b[i], b[max_row] = b[max_row], b[i]

        for j in range(i+1, n):
            factor = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= factor * a[i][k]
            b[j] -= factor * b[i]

    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        sum_ax = sum(a[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - sum_ax) / a[i][i]

    return x

a = [[3, 2, 1],
     [2, 3, 2],
     [1, 2, 3]]
b = [1, 2, 3]

result = gauss_elimination(a,b)
print("Solution:", result)
