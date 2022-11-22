"""
Gauss elimination method for solving system of linear equations.
"""
from typing import List

import numpy as np


def back_substitution(aug_matrix: np.ndarray, n: int) -> List:

    ans_vec = [0 for i in range(n)]
    ans_vec[n - 1] = aug_matrix[n - 1][n] / aug_matrix[n - 1][n - 1]

    for i in range(n - 1, -1, -1):
        ans_vec[i] = aug_matrix[i][n]

        for j in range(i + 1, n):
            ans_vec[i] = ans_vec[i] - aug_matrix[i][j] * ans_vec[j]

        ans_vec[i] = ans_vec[i] / aug_matrix[i][i]

    return ans_vec


def gauss_elimination(matrix: np.ndarray, vec_of_unknowns: np.ndarray) -> List:
    aug_matrix = np.hstack((matrix, vec_of_unknowns))
    n = vec_of_unknowns.shape[0]

    for i in range(0, n - 1):
        if aug_matrix[i][i] == 0.0:
            raise RuntimeError("Unable to create Upper Triangular Matrix")

        for j in range(i + 1, n):
            ratio = aug_matrix[j][i] / aug_matrix[i][i]

            for k in range(0, n + 1):
                aug_matrix[j][k] = aug_matrix[j][k] - ratio * aug_matrix[i][k]

    return back_substitution(aug_matrix, n)
