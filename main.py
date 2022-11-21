import numpy as np
import scipy


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
        tmp = np.random.randint(0, 10, size=(1,1))
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


def write_to_file_true(file_num, coef_mat, vec, ans):
    with open("equations/sample_desparse_" + str(file_num) + ".py", 'w', encoding='UTF-8') as file:
        file.write("matrix = " + coef_mat.tolist().__str__() + "\n")
        file.write("vec = " + vec.reshape(1, 1000).tolist().__str__() + "\n")
        file.write("correct_ans = " + ans.reshape(1, 1000).tolist().__str__() + "\n")


def main():
    a, b, c = Sparse_matrix(1000)
    write_to_file_true(1, a.round(4), b.round(4), c.round(4))
    a, b, c = Dense_matrix(1000)
    write_to_file_true(2, a.round(4), b.round(4), c.round(4))


if __name__ == '__main__':
    main()
