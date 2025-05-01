def lu_decomposition(a):
    n = len(a)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            s = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = a[i][k] - s

        L[i][i] = 1 
        for k in range(i+1, n):
            s = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (a[k][i] - s) / U[i][i]

    return L, U

a = [[10, 1, 2],
     [1, 10, 1],
     [2, 1, 10]]

L, U = lu_decomposition(a)

print("L matrix:")
for row in L:
    print(row)

print("\nU matrix:")
for row in U:
    print(row)
