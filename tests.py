import unittest

from algorithms import gauss_elimination as gauel
from algorithms import seidel
from algorithms import tridiagonal_matrix_algorithm as trimatal

from equations.sample1 import matrix as coef_mat1, vec as vec1, correct_ans as ans1, corr_coef as coef1
from equations.sample2 import matrix as coef_mat2, vec as vec2, correct_ans as ans2, corr_coef as coef2
from equations.sample3 import matrix as coef_mat3, vec as vec3, correct_ans as ans3, corr_coef as coef3


class TestSoLAEMethods(unittest.TestCase):

    def test_gauss_elimination_method_1(self):
        test = gauel.gauss_elimination(coef_mat1, vec1)
        self.assertEqual(ans1, test)

    def test_gauss_elimination_method_2(self):
        test = gauel.gauss_elimination(coef_mat2, vec2)
        self.assertEqual(ans2, test)

    def test_gauss_elimination_method_3(self):
        test = gauel.gauss_elimination(coef_mat3, vec3)
        self.assertEqual(ans3, test)

    def test_seidel_method_1(self):
        test = seidel.Zeydel(coef_mat1, vec1, coef1)
        self.assertEqual(ans1, test)

    def test_seidel_method_2(self):
        test = seidel.Zeydel(coef_mat2, vec2, coef2)
        self.assertEqual(ans2, test)

    def test_seidel_method_3(self):
        test = seidel.Zeydel(coef_mat3, vec3, coef3)
        self.assertEqual(ans3, test)

    def test_tridiagonal_matrix_algorithm_1(self):
        test = trimatal.backward(coef_mat1, vec1)
        self.assertEqual(ans1, test)

    def test_tridiagonal_matrix_algorithm_2(self):
        test = trimatal.backward(coef_mat2, vec2)
        self.assertEqual(ans2, test)

    def test_tridiagonal_matrix_algorithm_3(self):
        test = trimatal.backward(coef_mat3, vec3)
        self.assertEqual(ans3, test)

