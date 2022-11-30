# Numerical methods for solving system of algebraic linear equations.
## Responsibilities

### Всегда подается квадратная матрица любой размерности NxN и горизонтальный вектор вектор размерности 1xN

### Чтобы использовать методы нужно испортировать данный фрагмент кода:

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

### Чтобы запустить метод, который нам нужен:
seidel.Zeydel(matrix,vec)  - Решение СЛАУ с помощью метода Зейделя.
lude.solve_LU(matrix,vec)  - Решение СЛАУ с помощью LU-разложения.
gaule.solve(matrix,vec) - Метод Гаусса с выбором ведущего элемента по столбцам.
trimatal.transfiguration(matrix,vec)  - Тридиагональный матричный алгоритм.
sim.SimpleIt(matrix,vec) - Метод простых итераций.
gauel.gauss_elimination(matrix,vec) - Метод Гаусса с исключением.
gausm.gauss(matrix,vec) - Метод Гаусса.

- Alexander "[@oCatano](https://github.com/oCatano)" Aivazov - LU Decomposition method, library usage examples
- Akopyan "[@Bastard12](https://github.com/Bastard12)" Ruslan - Gauss-Seidel method
- Baslin "[@SheezZarR](https://github.com/SheezZarR)" Iaroslav - Gauss elimination method, testing
- Kurbet "[@ziabric](https://github.com/ziabric)" Nikita, Urkov "[SuperPizza303](https://github.com/SuperPizza303)" Pavel - Gauss Method
- Khachatryan "[@Artemkat17](https://github.com/Artemkat17)" Artem, Leschinskas Edvard - Simple Iteration Method
- Samoylenko "[@Starman-in-the-Sky](https://github.com/Starman-in-the-sky)" Michael - Tridiagonal Method
- Radionov "[@DeniRadionov](https://github.com/DeniRadionov)" Deni - Gauss Pivoting method
- Udin Kirill - Testing and data generation
