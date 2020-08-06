from polynomial import Polynomial, make_it_nice

''''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Полином наименьших квадратов
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


def Σ(xa: list, degree) -> float:
    a = float(0)

    for i in range(len(xa)):
        a += xa[i] ** degree

    return a


def Σ(xa: list, ya: list, degree) -> float:
    a = float(0)

    for i in range(len(xa)):
        a += (xa[i] ** degree) * ya[i]

    return a


def solve_gauss(matrix) -> list:
    n = len(matrix)
    
    for k in range(n - 1):
        for i in range(k + 1, n):
            div = matrix[i][k] / matrix[k][k]
            matrix[i][-1] -= div * matrix[k][-1]

            for j in range(k, n):
                matrix[i][j] -= div * matrix[k][j]

    x = [0 for i in range(n)]

    for k in range(n - 1, -1, -1):
        x[k] = (matrix[k][-1] - sum([matrix[k][j] * x[j] for j in range(k + 1, n)])) / matrix[k][k]

    return x


def square_polynomial(xa: list, ya: list, ma) -> Polynomial:
    matrix = [[Σ(xa, int(i + j)) for i in range(ma + 1)] + [Σ(xa, ya, j)] for j in range(ma + 1)]

    print(matrix)

    result = solve_gauss(matrix)

    while len(result) != len(xa):
        result += [0]

    print(result)

    return make_it_nice(result[::-1])
