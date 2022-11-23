from copy import deepcopy
import numpy as np
eps = 1e-10    # погрешность


def maxelement(a, col, count_swap):
    n = len(a)
    maxel = a[col][col]
    maxrow = col
    for i in range(col + 1, n):
        if maxel < abs(a[i][col]):
            maxel = abs(a[i][col])
            maxrow = i
    if col != maxrow:
        swap(a, maxrow, col)
        count_swap += 1
    return count_swap


def checkByZero(q):
    if abs(q) < eps:
       return 1


def determinant(a, count_swap):
    det = 1
    n = len(a)
    if count_swap % 2:
        count_swap = -1
    else:
        count_swap = 1
    for i in range(n):
        det *= a[i][i]
    det *= count_swap
    return det


def swap(a, row_one, row_two=0):
    n = len(a)
    for i in range(n + 1):
        tmp = a[row_one][i]
        a[row_one][i] = a[row_two][i]
        a[row_two][i] = tmp



def sub(a, row_one, row_two, mn=1):
    n = len(a)
    for i in range(n + 1):
        a[row_one][i] -= a[row_two][i] * mn
    return a


def triangle(a):
    n = len(a)
    count_swap = 0
    for j in range(n):
        count_swap = maxelement(a, j, count_swap)
        for i in range(j + 1, n):
            c = a[i][j] / a[j][j]
            sub(a, i, j, c)
    return count_swap


def searchSolution(a):
    n = len(a)
    solution = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        solution[i] = round(a[i][n] / a[i][i])
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
    count_swap = triangle(a)
    det = determinant(a, count_swap)
    flag = checkByZero(det)
    if flag:
        print("\nМатрица вырожденная. Определитель равен нулю\n")
        exit(1)
    x = searchSolution(a)
    return x


def matrix_mul(a, x):
    n = len(a)
    m = len(x)
    result = []
    for i in range(n):
        s = 0
        for j in range(m):
            s += x[j] * a[i][j]
        result.append(s)
    return result


def matrix_mul_2(a, b):
    n = len(a)
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k] * b[k][j]
    return res


def getVectorB(a):
    n = len(a)
    vectorB = []
    for i in range(n):
        vectorB.append(a[i][n])
    return vectorB


def getVectorA(a):
    vectorA = a[:]
    return vectorA


def discrepancy(res, b):
    for i in range(len(b)):
        res[i] = b[i] - res[i]
    return res


def inverse(a):
    n = len(a)
    inv = [[0 for i in range(len(a) + 1)] for j in range(len(a))]
    for i in range(n):
        for j in range(n):
            if i == j:
                a[j][n] = 1.0
            else:
                a[j][n] = 0.0
        q = copy.deepcopy(a)
        vec_sol = gauss(q)
        for k in range(len(vec_sol)):
            inv[k][i] = vec_sol[k]
    return inv


def norm(a):
    n = len(a)
    max = 0
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += abs(a[i][j])
            if max < sum:
                max = sum
    return max


def condition_number(norm_one, norm_two):
    cond = norm_one * norm_two
    return cond
