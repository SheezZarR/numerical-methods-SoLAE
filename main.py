from typing import List
import copy
import time
import scipy
from algorithms import gauss_elimination as gauel
from algorithms import gauss_method as gausm
from algorithms import gauss_leader as gaule
from algorithms import tridiagonal_matrix_algorithm as trimatal
from algorithms import seidel
from algorithms import Simple_Iteration as sim
from algorithms import LU_decomposition as lude
import numpy as np


def solve(coef_matr: List[list], free_coef: list) -> np.array:
    """
    main function, which solve SoLAE
    :coef_matr: matrix of coefficients (List[List] or numpy.ndarray)
    :free_coef: vector of free coefficients (List or numpy.ndarray)
    :return: np.array
    """
    if not (isinstance(coef_matr, list) or isinstance(coef_matr, np.ndarray)):
        raise TypeError("coef_matr should be list or numpy.ndarray")
    if not (isinstance(free_coef, list) or isinstance(free_coef, np.ndarray)):
        raise TypeError("free_coef should be list or numpy.ndarray")
    for vec in coef_matr:
        if not (isinstance(vec, list) or isinstance(vec, np.ndarray)):
            raise TypeError("coef_matr should be list[list] or numpy.ndarray")

    if abs(np.linalg.det(coef_matr)) < 0.0000001:
        raise Exception("Determenant is equal to zero")

    algos_arr = [seidel.Zeydel, lude.solve_LU, gaule.solve, trimatal.transfiguration,
                 sim.SimpleIt, gauel.gauss_elimination, gausm.gauss]

    for method in algos_arr:
        try:
            return method(copy.deepcopy(coef_matr), copy.deepcopy(free_coef))
        except:
            pass

    return np.linalg.solve(coef_matr, free_coef)


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


def speed_test():
    algos_arr = [gauel.gauss_elimination, lude.solve_LU, gaule.solve, gausm.gauss,
                 trimatal.transfiguration, seidel.Zeydel, sim.SimpleIt, ]

    A = np.random.randint(1, 10, (3, 3))
    b = np.random.randint(5, 8, (3, 1))
    print(A)
    print(b)
    true_ans = np.linalg.solve(A, b)
    print(true_ans[:6])
    print("********************")
    time_matr = []
    for i, item in enumerate(algos_arr):
        try:
            start = time.time()
            print(solve(A, b))
            print(time.time() - start)
        except:
            print(i)
    print('time= ', time_matr)
    print('************')
    A, b, x = Sparse_matrix(120)
    time_matr = []
    for i, item in enumerate(algos_arr):
        try:
            start = time.time()
            solve(A,b)
            print(time.time() - start)
        except:
            print(i)


if __name__ == '__main__':
    speed_test()


