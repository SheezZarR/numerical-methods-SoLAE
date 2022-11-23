from typing import List
import scipy
import algorithms as alg
import numpy as np


def solve(coef_matr: List[list], free_coef: list) -> np.array:
    Zeidel_conditional = True
    if not isinstance(coef_matr, list):
        raise TypeError("coef_matr should be list")
    if not isinstance(free_coef, list):
        raise TypeError("free_coef should be list")
    for vec in coef_matr:
        if not isinstance(vec, list):
            raise TypeError("coef_matr should be list[list]")

    for i in range(len(coef_matr)):
        ma = max(abs(coef_matr[i]))

        if ma <= (sum(abs(coef_matr[i])) - ma):
            Zeidel_conditional = False

    if abs(np.linalg.det(coef_matr)) < 0.0000001:
        pass

    else:
        raise ValueError("Determenant is equal to zero")


def Sparse_matrix(n: int):
    """
    Ax = b

    params: n - размер матрицы

    return:

    A - matrix [n, n]
    b - array [n, 1]
    x - array [n, 1]

    """

    np.random.seed(50)

    A = scipy.sparse.random(n, n, density=0.25)
    A = A.toarray()
    A = np.matrix(A)

    for i in range(n):
        tmp = np.random.randint(0, 10, size=(1, 1))
        A[i] = A[i] * 10

        break

    A.round(2)
    b = np.random.rand(n) + np.random.randint(0, 2 * n, size=(1, n))
    b = b.reshape(n, 1)

    x = np.linalg.solve(A, b)
    return A, b, x


def Dense_matrix(n: int):
    """
    Ax = b

    params: n - размер матрицы

    return:

    A - matrix [n, n]
    b - array [n, 1]
    x - array [n, 1]

    """

    np.random.seed(21)

    A = np.random.rand(n, n)
    for i in range(A.shape[0]):
        A[i] = A[i] + np.random.randint(1, 30, size=(1, n))
    b = np.random.rand(n) + np.random.randint(1, 50, size=(1, n))
    b = b.reshape(n, 1)
    x = np.linalg.solve(A, b)
    return A, b, x


def three_diag_matrix_generator(n: int):
    n = 10
    A = np.zeros(shape=(n, n))
    for i in range(-1, 1):
        d = np.diagflat(np.random.randint(1, 21, n - (i % 2)), i)
        A = A + d
    d = np.diagflat(np.random.randint(40, 81, n - 1), 1)
    A = A + d
    b = np.random.randint(50, 160, size=(n, 1))
    x = np.linalg.solve(A, b)
    return A, b, x


def write_to_file_true(file_num, coef_mat, vec, ans):
    with open("equations/sample_desparse_" + str(file_num) + ".py", 'w', encoding='UTF-8') as file:
        file.write("matrix = " + coef_mat.tolist().__str__() + "\n")
        file.write("vec = " + vec.reshape(1, vec.shape[0]).tolist().__str__() + "\n")
        file.write("correct_ans = " + ans.reshape(1, ans.shape[0]).tolist().__str__() + "\n")


def main():
    # a, b, c = Sparse_matrix(1000)
    # write_to_file_true(1, a.round(4), b.round(4), c.round(4))
    # a, b, c = Dense_matrix(1000)
    # write_to_file_true(2, a.round(4), b.round(4), c.round(4))
    a, b, c = three_diag_matrix_generator(3)
    write_to_file_true(3, a.round(4), b.round(4), c.round(4))


if __name__ == '__main__':
    main()
