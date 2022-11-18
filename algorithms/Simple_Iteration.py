# метод простой итерации
import numpy as np
from math import *


def Corr(A, b):
    in_ = 0
    indMax = [0 for i in range(len(A))]
    for i in range(len(A)):
        ma = max(abs(A[i]))
        if ma <= (sum(abs(A[i])) - ma):
            raise ValueError(
                "Every row should have an element which absolute value is bigger than sum of other elements absolute values in row")

        for j in range(len(A)):
            if abs(A[i][j]) == ma:
                indMax[i] = j
                break

    for i in range(len(indMax)):
        for j in range(i + 1, len(indMax)):
            if indMax[i] == indMax[j]:
                raise ValueError('All biggest elements in the rows should be in different columns')

    for i in range(len(A)):
        if indMax[i] != i:
            ind_ = 0
            for j in range(len(indMax)):
                if indMax[j] == i:
                    ind_ = j
            for j in range(len(A)):
                val1 = A[i][j]
                A[i][j] = A[ind_][j]
                A[ind_][j] = val1
            val2 = b[i]
            b[i] = b[ind_]
            b[ind_] = val2
            val = indMax[i]
            indMax[i] = indMax[ind_]
            indMax[ind_] = val
    for i in range(len(A)):
        z = A[i][i]
        for j in range(len(A)):
            A[i][j] /= z
        b[i] /= z
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                A[i][j] = 0
            else:
                A[i][j] *= -1
    return A, b


def proverka(x, xPrev):
    a = [0. for i in range(len(x))]
    for i in range(len(x)):
        a[i] = abs(x[i] - xPrev[i])
    return max(a)


def SimpleIt(A, b, eps=0.001):
    A, b = np.array(A), np.array(b)
    A, b = A.astype(float), b.astype(float)
    m = len(A)
    x = [0. for i in range(m)]
    A, b = Corr(A, b)
    count = 0
    pogr = 0
    prev = [1. for i in range(m)]
    while (proverka(x, prev) >= eps or count == 0):
        for i in range(m):
            prev[i] = x[i]
        for i in range(m):
            s = 0
            for j in range(m):
                s += A[i][j] * prev[j]
            x[i] = (s + b[i])
        count += 1
    return x

