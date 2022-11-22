import numpy as np


def three_diag_check(m):
    tmp = True
    for i in range(0, len(m) - 2):
        for j in range(2 + i, len(m)):
            if(m[i][j] != 0):
                tmp = False
            if(m[len(m) - 1 - i][len(m) - 1 - j] != 0):
                tmp = False
    return tmp


'''Функция проверки на правильность трёхдиагональной матрицы'''


def forward(m):
    arr = [0] * 2 * len(m)
    arr[0] = round(m[0][1]/(-m[0][0]), 2)
    arr[1] = round(m[0][len(m[0]) - 1]/(m[0][0]), 2)
    for i in range(1, len(m) - 1):
        arr[i * 2] = round(m[i][i + 1]/(-m[i][i] - m[i][i - 1] * arr[i * 2 - 2]), 2)
        arr[i * 2 + 1] = round((m[i][i - 1] * arr[i * 2 + 1 - 2] - m[i][len(m[0]) - 1])/(-m[i][i] - m[i][i - 1] * arr[i * 2 - 2]), 2)
    return arr


'''Функция прямого хода'''


def backward(m, k):
    xarr = np.array([0] * len(m))
    k[len(k) - 1] = round((m[len(m) - 1][len(m) - 1 - 1] * k[len(m) - 1 * 2 + 1 - 2] - m[len(m) - 1][len(m[0]) - 1])/(-m[len(m) - 1][len(m) - 1] - m[len(m) - 1][len(m) - 1 - 1] * k[len(m) - 1 * 2 - 2]), 2)
    xarr[len(m) - 1] = k[len(k) - 1]
    for i in range(len(m) - 2, -1, -1):
        xarr[i] = round(k[i * 2] * xarr[i + 1] + k[i * 2 + 1], 1)
    return xarr


'''Функция обратного хода'''


if __name__ == '__main__':
    mat = np.array([[5, 3, 0, 0, 8], [3, 6, 1, 0, 10], [0, 1, 4, -2, 3], [0, 0, 1, -3, -2]])
    if(three_diag_check(mat) != True):
        print("Заданная матрица не соответствует выбранному методу решения")
    else:
        print(backward(mat, forward(mat)))
