import numpy as np


def bubble_max_row(m, col):
    save = m
    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i

    if max_row != col:
        m[[max_row, col]] = m[[col, max_row]]


def solve(m, X):
    m[0][0] *= 1.0
    sa = len(X)
    mas = []
    n = len(m)
    X = X.transpose()
    for i in range(sa):
        mas.append([0] * 1)
        mas[i][0] = X[i]
    m = np.hstack((m, mas))

    for k in range(n - 1):
        bubble_max_row(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]

            m[i][-1] -= div * m[k][-1]

            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    if is_singular(m):
        print('The system has infinite number of answers.')
        return

    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]
    return x


def is_singular(m):
    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False


