from typing import List

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

        if ma <= (sum(abs(coef_matr[i]))-ma):
            Zeidel_conditional = False



    if abs(np.linalg.det(coef_matr)) < 0.0000001:
        pass

    else:
        raise ValueError("Determenant is equal to zero")
