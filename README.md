# Numerical methods for solving system of algebraic linear equations.

## Разработчики:
- Alexander "[@oCatano](https://github.com/oCatano)" Aivazov - LU Decomposition method, library usage examples
- Akopyan "[@Bastard12](https://github.com/Bastard12)" Ruslan - Gauss-Seidel method
- Baslin "[@SheezZarR](https://github.com/SheezZarR)" Iaroslav - Gauss elimination method, testing
- Kurbet "[@ziabric](https://github.com/ziabric)" Nikita, Urkov "[SuperPizza303](https://github.com/SuperPizza303)" Pavel - Gauss Method
- Khachatryan "[@Artemkat17](https://github.com/Artemkat17)" Artem, Leschinskas Edvard - Simple Iteration Method
- Samoylenko "[@Starman-in-the-Sky](https://github.com/Starman-in-the-sky)" Michael - Tridiagonal Method
- Radionov "[@DeniRadionov](https://github.com/DeniRadionov)" Deni - Gauss Pivoting method
- Udin Kirill - Testing and data generation

### Всегда подается квадратная матрица любой размерности NxN и горизонтальный вектор размерности 1xN.

### Вызов main функции.
```python 
 """
    main function, which solve SoLAE
    :coef_matr: matrix of coefficients (List[List] or numpy.ndarray)
    :free_coef: vector of free coefficients   (List or numpy.ndarray)
    :return: np.array
    """
   import main as own
   own.solve(coef_matr: List[list], free_coef: list)
   ```
### Решение СЛАУ с помощью метода Зейделя.
```python 
   from algorithms import seidel 
   seidel.Zeydel(matrix,vec) 
   ```

### Решение СЛАУ с помощью LU-разложения.
```python 
from algorithms import LU_decomposition as lude
lude.solve_LU(matrix,vec) 
```

### Метод Гаусса с выбором ведущего элемента по столбцам.
```python 
from algorithms import gauss_leader as gaule
gaule.solve(matrix,vec) 
```

### Тридиагональный матричный алгоритм.
```python 
from algorithms import tridiagonal_matrix_algorithm as trimatal
trimatal.transfiguration(matrix,vec) 
```
### Метод простых итераций.
```python 
from algorithms import Simple_Iteration as sim
sim.SimpleIt(matrix,vec) 
```

### Метод Гаусса с исключением.
```python 
from algorithms import gauss_elimination as gauel
gauel.gauss_elimination(matrix,vec) 
```

### Метод Гаусса.
```python 
from algorithms import gauss_method as gausm
gausm.gauss(matrix,vec) 
```

