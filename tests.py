import unittest

import numpy as np

from algorithms import gauss_elimination as gauel
from algorithms import gauss_method as gausm
from algorithms import gauss_leader as gaule
from algorithms import tridiagonal_matrix_algorithm as trimatal
from algorithms import seidel
from algorithms import Simple_Iteration as sim
from algorithms import LU_decomposition as lude


from equations.tridiagonal_sample import matrix as tridiag_m, vec as tridiag_v, correct_ans as tridiag_ans

from equations.sample1 import matrix as coef_mat1, vec as vec1, correct_ans as ans1, corr_coef as coef1
from equations.sample2 import matrix as coef_mat2, vec as vec2, correct_ans as ans2, corr_coef as coef2
from equations.sample3 import matrix as coef_mat3, vec as vec3, correct_ans as ans3, corr_coef as coef3
from equations.sample_desparse_1 import matrix as coef_mat4, vec as vec4, correct_ans as ans4
from equations.sample_desparse_2 import matrix as coef_mat5, vec as vec5, correct_ans as ans5


def cook_data(matrix, vec) -> (np.ndarray, np.ndarray):
    return (
        np.ndarray(
            shape=(len(matrix), len(matrix)),
            buffer=np.array([np.array(row) for row in matrix], dtype=float),
            dtype=float
        ),
        np.ndarray(
            shape=(len(vec), 1),
            buffer=np.array([column for column in vec], dtype=float),
            dtype=float
        )
    )


class TestGausMethod(unittest.TestCase):
    """Test cases for gaussian method."""
    def test_gauss_method_1(self):
        cfm, vc = cook_data(coef_mat1, vec1)
        test = gausm.gauss(cfm, vc)
        self.assertEqual(test, ans1)


class TestGauelMethod(unittest.TestCase):
    """Test cases for gauss elimination method."""

    def test_gauss_elimination_method_1(self):
        cfm, vc = cook_data(coef_mat1, vec1)
        test = gauel.gauss_elimination(cfm, vc)
        self.assertEqual(ans1, test)

    def test_gauss_elimination_method_2(self):
        cfm, vc = cook_data(coef_mat2, vec2)
        test = gauel.gauss_elimination(cfm, vc)
        self.assertEqual(ans2, test)

    def test_gauss_elimination_method_3(self):
        cfm, vc = cook_data(coef_mat3, vec3)
        test = gauel.gauss_elimination(cfm, vc)
        self.assertEqual(ans3, test)

    def test_gauss_elimination_method_4(self):
        cfm, vs = cook_data(coef_mat5, vec5)
        test = gauel.gauss_elimination(cfm, vs)

        self.assertEqual(test, ans5)


class TestGauPivotingMethod(unittest.TestCase):
    """Test cases for gauss with pivoting."""

    def test_gauss_pivoting_method(self):
        cfm, vc = cook_data(coef_mat1, vec1)
        test = gaule.solve(cfm, vc)
        self.assertEqual(test, ans1)


class TestTridiagonalMethod(unittest.TestCase):
    """Test cases for tridiagonal matrix method."""

    def test_tridiagonal_matrix_algorithm_1(self):
        self.assertRaises(ValueError, trimatal.backward(coef_mat1, vec1))

    def test_tridiagonal_matrix_algorithm_4(self):
        cfm, vc = cook_data(tridiag_m, tridiag_v)
        test = trimatal.backward(cfm, vc)
        self.assertEqual(tridiag_ans, test)


class TestLUDecompMethod(unittest.TestCase):
    """Test cases for LU decomposition method."""

    def test_LU_Decomposition_method_1(self):
        test = lude.solve_LU(coef_mat1, vec1)
        self.assertEqual(test, ans1)

    def test_LU_Decomposition_method_2(self):
        test = lude.solve_LU(coef_mat2, vec2)
        self.assertEqual(ans2, test)

    def test_LU_Decomposition_method_3(self):
        test = lude.solve_LU(coef_mat3, vec3)
        self.assertEqual(ans3, test)

    def test_LU_Decomposition_method_4(self):
        test = lude.solve_LU(coef_mat5, vec5)
        self.assertEqual(ans5, test)


class TestSimpleIterMethod(unittest.TestCase):
    """Test cases for simple iteration method."""
    def test_Simple_Iter_method_incorrect_input(self):
        cfm, vc = cook_data(coef_mat1, vec1)
        self.assertRaises(ValueError, sim.SimpleIt(cfm, vc))

    def test_Simple_Iter_method_correct_input(self):
        cfm, vc = cook_data(coef_mat3, vec3)
        test = sim.SimpleIt(cfm, vc)
        self.assertEqual(ans3, test)


class TestSeidelMethod(unittest.TestCase):
    """Test cases for Seidel method."""

    def test_seidel_method_incorrect_input(self):
        self.assertRaises(ValueError, seidel.Zeydel(coef_mat1, vec1, coef1))

    def test_seidel_method_correct_input(self):
        test = seidel.Zeydel(coef_mat3, vec3, coef3)
        self.assertEqual(ans3, test)

