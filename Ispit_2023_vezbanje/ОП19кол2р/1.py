X = [
    [1, 2, 3],
    [3,-1, 4],
    [2, 0, 1]
]

Y = [
    [ 1, -1],
    [-2,  3],
    [-1,  2]
]
rezultat = [[0] * len(Y[0]) for _ in range(len(X))]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            rezultat[i][j] += X[i][k] * Y[k][j]

print('\nRezultat:')
for x in rezultat:
    print(x)