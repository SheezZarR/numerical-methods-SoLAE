import unittest

from algorithms import gauss_elimination as gauel
from algorithms import seidel
from algorithms import tridiagonal_matrix_algorithm as trimatal
from algorithms import Simple_Iteration as sim

from equations.tridiagonal_sample import matrix as tridiag_m, vec as tridiag_v, correct_ans as tridiag_ans

from equations.sample1 import matrix as coef_mat1, vec as vec1, correct_ans as ans1, corr_coef as coef1
from equations.sample2 import matrix as coef_mat2, vec as vec2, correct_ans as ans2, corr_coef as coef2
from equations.sample3 import matrix as coef_mat3, vec as vec3, correct_ans as ans3, corr_coef as coef3


class TestGausMethod(unittest.TestCase):
    """Test cases for gaussian method."""


class TestGauelMethod(unittest.TestCase):
    """Test cases for gauss elimination method."""

    def test_gauss_elimination_method_1(self):
        test = gauel.gauss_elimination(coef_mat1, vec1)
        self.assertEqual(ans1, test)

    def test_gauss_elimination_method_2(self):
        test = gauel.gauss_elimination(coef_mat2, vec2)
        self.assertEqual(ans2, test)

    def test_gauss_elimination_method_3(self):
        test = gauel.gauss_elimination(coef_mat3, vec3)
        self.assertEqual(ans3, test)


class TestGauPivotingMethod(unittest.TestCase):
    """Test cases for gauss with pivoting."""
    pass


class TestTridiagonalMethod(unittest.TestCase):
    """Test cases for tridiagonal matrix method."""

    def test_tridiagonal_matrix_algorithm_1(self):
        test = trimatal.backward(coef_mat1, vec1)
        self.assertEqual(ans1, test)

    def test_tridiagonal_matrix_algorithm_2(self):
        test = trimatal.backward(coef_mat2, vec2)
        self.assertEqual(ans2, test)

    def test_tridiagonal_matrix_algorithm_3(self):
        test = trimatal.backward(coef_mat3, vec3)
        self.assertEqual(ans3, test)

    def test_tridiagonal_matrix_algorithm_4(self):
        test = trimatal.backward(tridiag_m, tridiag_v)
        self.assertEqual(tridiag_ans, test)


class TestLUDecompMethod(unittest.TestCase):
    """Test cases for LU decomposition method."""
    pass


class TestSimpleIterMethod(unittest.TestCase):
    """Test cases for simple iteration method."""
    def test_Simple_Iter_method_1(self):
        test = sim.SimpleIt(coef_mat1, vec1)
        self.assertEqual(ans1, test)

    def test_Simple_Iter_method_2(self):
        test = sim.SimpleIt(coef_mat2, vec2)
        self.assertEqual(ans2, test)

    def test_Simple_Iter_method_3(self):
        test = sim.SimpleIt(coef_mat3, vec3)
        self.assertEqual(ans3, test)


class TestSeidelMethod(unittest.TestCase):
    """Test cases for Seidel method."""

    def test_seidel_method_1(self):
        test = seidel.Zeydel(coef_mat1, vec1, coef1)
        self.assertEqual(ans1, test)

    def test_seidel_method_2(self):
        test = seidel.Zeydel(coef_mat2, vec2, coef2)
        self.assertEqual(ans2, test)

    def test_seidel_method_3(self):
        test = seidel.Zeydel(coef_mat3, vec3, coef3)
        self.assertEqual(ans3, test)
