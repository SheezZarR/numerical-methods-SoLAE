import unittest

from algorithms import gauss_elimination as gauel
from algorithms import seidel
from algorithms import tridiagonal_matrix_algorithm as trimatal

from equations.sample1 import matrix as coef_mat1, vec as vec1, correct_ans as ans1, corr_coef
from equations.sample2 import matrix as coef_mat2, vec as vec2, correct_ans as ans2, corr_coef
from equations.sample3 import matrix as coef_mat3, vec as vec3, correct_ans as ans3, corr_coef


class TestSoLAEMethods(unittest.TestCase):

    def method_tests(self, method_to_test):
        test_1 = method_to_test(coef_mat1, vec1, corr_coef)
        self.assertEqual(ans1, test_1)

        test_2 = method_to_test(coef_mat2, vec2, corr_coef)
        self.assertEqual(ans2, test_2)

        test_3 = method_to_test(coef_mat3, vec3, corr_coef)
        self.assertEqual(ans3, test_3)

    def test_gauss_elimination_method(self):
        self.method_tests(gauel.gauss_elimination)

    def test_seidel_method(self):
        self.method_tests(seidel.Zeydel)

    def test_tridiagonal_matrix_algorithm(self):
        self.method_tests(trimatal.backward)

