import numpy as np


def bubble_max_row(m, col):
    """Replace m[col] row with the one of the underlying rows with the modulo greatest first element.
    :param m: matrix (list of lists)
    :param col: index of the column/row from which underlying search will be launched
    :return: None. Function changes the matrix structure.
    """
    max_element = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_element):
            max_element = m[i][col]
            max_row = i
    if max_row != col:
        m[col], m[max_row] = m[max_row], m[col]


def solve(m, X):
    """Solve linear equations system with gaussian method.
    :param m: matrix (list of lists)
    """
    nn = len(X)
    for i in range(nn):
        m[i].append(X[i])
    n = len(m)
    # forward trace
    for k in range(n - 1):
        bubble_max_row(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]

            m[i][n] -= div * m[k][n]

            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    # check modified system for nonsingularity
    if is_singular(m):
        print('The system has infinite number of answers...')
        return

    # backward trace
    x = [0 for i in range(n)]
    for k in range(n - 1, -1, -1):
        x[k] = (m[k][-1] - sum([m[k][j] * x[j] for j in range(k + 1, n)])) / m[k][k]
    return x


def is_singular(m):
    """Check matrix for nonsingularity.
    :param m: matrix (list of lists)
    :return: True if system is nonsingular
    """

    for i in range(len(m)):
        if not m[i][i]:
            return True
    return False


"""if __name__ == "__main__":    
    #m = [[2, 2, 3, 1 ], [1, -1, 0, 0], [-1, 2, 1, 2]]

    m = [[2, 2, 3 ], [1, -1, 0], [-1, 2, 1]]
    X=[1, 0 , 2]

    print(solve(m, X))"""