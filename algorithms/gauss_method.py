from copy import deepcopy
import numpy as np
eps = 1e-10    # погрешность


def maxelement(a, col, count_swap):
    maxel = a[col][col]
    maxrow = col
    for i in range(col + 1, len(a)):
        if maxel < abs(a[i][col]):
            maxel = abs(a[i][col])
            maxrow = i
    if col != maxrow:
        a[maxrow], a[col] = a[col], deepcopy(a[maxrow])
        count_swap += 1
    return count_swap


def determinant(a, count_swap):
    det = 1
    if count_swap % 2:
        count_swap = -1
    else:
        count_swap = 1
    for i in range(len(a)):
        det *= a[i][i]
    det *= count_swap
    return det


def sub(a, row_one, row_two, mn=1):
    for i in range(len(a) + 1):
        a[row_one][i] -= a[row_two][i] * mn
    return a


def triangle(a):
    n = len(a)
    count_swap = 0
    print(n)
    for j in range(n):
        count_swap = maxelement(a, j, count_swap)
        for i in range(j + 1, n):
            c = a[i][j] / a[j][j]
            sub(a, i, j, c)
        #print(j)
    return count_swap


def searchSolution(a):
    n = len(a)
    solution = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        solution[i] = a[i][n] / a[i][i]
        #   print("solution =", solution)
        for j in range(i - 1, -1, -1):
            a[j][n] -= a[j][i] * solution[i]

    return solution


def gauss(a, vec):
    a = deepcopy(a)
    a = list(a)
    for _ in range(len(a)):
        a[_] = list(a[_])
        a[_].append(vec[_][0])
    a = np.array(a)
    #print("1")
    count_swap = triangle(a)
    #print("2")
    det = determinant(a, count_swap)
    flag = abs(det) < eps
    if flag:
        print("\nМатрица вырожденная. Определитель равен нулю\n")
        exit(1)
    #print("3")
    x = searchSolution(a)
    print()
    return x
