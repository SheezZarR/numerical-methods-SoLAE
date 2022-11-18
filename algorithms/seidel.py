from math import *
import numpy as np


def Corr(A, b):
    if len(A) != len(A[0]):
        raise Exception('Matrix must be square')
    if len(A) != len(b):
        raise Exception('The vector should contain n(number of our unknown variables) floats')

    in_ = 0
    for i in range(len(A)):
        ma = max(abs(A[i]))

        if ma <= (sum(abs(A[i]))-ma):
            raise Exception("Every row should have an element which absolute value is bigger than sum of other elements absolute values in row")
    for i in range(len(A)):
        ma = max(abs(A[i]))
        for j in range(len(A)):
            if A[i][j] == ma:
                in_ = j
                break

        if in_ != i:
            A[[i, in_]] = A[[in_, i]]
            b[[i, in_]] = b[[in_, i]]

    for i in range(len(A)):
        if abs(A[i][i]) != max(abs(A[i])):
            raise Exception("Use matrix which can be modified into a diagonally dominant one")

    for i in range(len(A)):
        z = A[i][i]
        for j in range(len(A)):
            A[i][j] /= z
        b[i] /= z
    return A, b

def Zeydel(A, b, e=5):
    e_ = pow(10, -e)
    A, b = np.array(A), np.array(b)
    A, b = A.astype(float), b.astype(float)
    m = len(A)
    x = [0. for i in range(m)]
    count = 0
    pogr = 0
    A, b = Corr(A, b)
    while True:
        x_new = np.copy(x)
        for i in range(m):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
            x_new[i] = b[i] - s1 - s2  # Получаем начальные значения для x1,x2,x3,...,xn
        #print(x_new)
        pogr = sum(abs(x_new[i] - x[i]) for i in range(m))  # погрешность
        if pogr < e_:
            break
        count += 1
        x = x_new
    x = np.round(x, e)
    x = list(x)
    return x
