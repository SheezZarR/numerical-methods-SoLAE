from math import *
import numpy as np


def Corr(A, b):
    if len(A) != len(A[0]):
        raise Exception('Matrix must be square')
    if len(A) != len(b):
        raise Exception('The vector should contain n(number of our unknown variables) floats')

    in_ = 0
    for i in range(len(A)):
        ma = max(A[i])
        if ma <= (sum(A[i])-ma):
            raise Exception("Every row should have an element which absolute value is bigger than sum of other elements absolute values in row")
        for j in range(len(A)):
            if A[i][j] == ma:
                in_ = j
                break
        if in_ != i:
            A[[i, in_]] = A[[in_, i]]
            b[[i,in_]] = b[[in_,i]]
    for i in range(len(A)):
        max_ = max(abs(A[i]))
        for j in range(len(A)):
            A[i][j] /= max_
        b[i][0] /= max_
    return A, b

def Zeydel(A, b, e):
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
            x_new[i] = (b[i] - s1 - s2)  # Получаем начальные значения для x1,x2,x3,...,xn
        pogr = sum(abs(x_new[i] - x[i]) for i in range(m))  # погрешность
        if pogr < e:
            break
        count += 1
        x = x_new
    return x
