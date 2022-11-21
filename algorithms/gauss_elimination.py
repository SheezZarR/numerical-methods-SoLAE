"""
Gauss elimination method for solving system of linear equations.
"""
from typing import List


def add_column(matrix: List[list], vec: list) -> List[list]:
    """Adds a vector to a matrix"""

    if len(matrix) != len(vec):
        raise RuntimeError(f"Wrong vector size")

    for i in range(len(matrix)):
        matrix[i].append(vec[i])

    return matrix


def back_substitution(aug_matrix: List[list], n: int) -> list:

    ans_vec = [0 for i in range(n)]
    ans_vec[n - 1] = aug_matrix[n - 1][n] / aug_matrix[n - 1][n - 1]

    for i in range(n - 1, -1, -1):
        ans_vec[i] = aug_matrix[i][n]

        for j in range(i + 1, n):
            ans_vec[i] = ans_vec[i] - aug_matrix[i][j] * ans_vec[j]

        ans_vec[i] = ans_vec[i] / aug_matrix[i][i]

    return ans_vec


def gauss_elimination(matrix: List[list], vec_of_unknowns: list) -> List[list]:
    aug_matrix = add_column(matrix, vec_of_unknowns)
    n = len(vec_of_unknowns)

    # Creation of Upper Triangular Matrix
    for i in range(0, n - 1):
        if aug_matrix[i][i] == 0.0:
            raise RuntimeError("Unable to create Upper Triangular Matrix")

        for j in range(i + 1, n):
            ratio = aug_matrix[j][i] / aug_matrix[i][i]

            for k in range(0, n + 1):
                aug_matrix[j][k] = aug_matrix[j][k] - ratio * aug_matrix[i][k]

    ans = back_substitution(aug_matrix, n)

    return ans
