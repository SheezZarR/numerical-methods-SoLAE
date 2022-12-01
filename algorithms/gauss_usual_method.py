import numpy as np


def changel(mat, i):
    tmp = mat[i][i]
    for j in range(i + 1, len(mat)):
        tmp2 = mat[j][i]
        for k in range(i, len(mat[j])):
            mat[j][k] = round(mat[j][k] - (mat[i][k] * tmp2 / tmp), 4)


def changeback(mat, i):
    tmp = mat[i][i]
    for j in range(i - 1, -1, -1):
        tmp2 = mat[j][i]
        for k in range(len(mat[j]) - 1, i - 1, -1):
            mat[j][k] = round(mat[j][k] - (mat[i][k] * tmp2 / tmp), 4)


def search(mat, i):
    tmp = 0
    for k in range(0, len(mat)):
        if(mat[k][i] != 0):
            tmp = k
    for k in range(0, len(mat[0])):
            mat[i][k] = round(mat[i][k] - mat[tmp][k])


def task1(pol):
    pol_copy = pol.copy()
    for i in range(0, len(pol_copy)):
        if(pol_copy[i][i] == 0):
            search(pol_copy, i)
    for i in range(0, len(pol_copy) - 1):
        changel(pol_copy, i)
    for i in range(len(pol_copy) - 1, 0, -1):
        changeback(pol_copy, i)
    ans = np.array([0] * len(pol), dtype = float)
    for i in range(0, len(pol)):
        ans[i] = pol_copy[i][len(pol_copy)] / pol_copy[i][i]
    return ans


def gauss_usual(matx, vec: np.ndarray):
    vec = vec.transpose()
    mat = np.array([[0] * (len(matx) + 1)] * len(matx[0]), dtype = float)
    for i in range(0, len(mat)):
        for j in range(0, len(mat)):
            mat[i, j] = matx[i, j]
        mat[i, len(mat)] = vec[i]
    return task1(mat)
