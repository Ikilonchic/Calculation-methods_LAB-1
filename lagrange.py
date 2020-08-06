from polynomial import Polynomial, make_it_nice, product_of_combinations

'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Полином Лагранжа
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


def calculate_k(i: int, xa: list, ya: list) -> float:
    result = ya[i]

    for j in range(len(xa)):
        if i != j:
            result /= xa[i] - xa[j]

    return result


def lagrange_polynomial(xa: list, ya: list) -> Polynomial:
    polynomial = [0] * len(xa)

    ks = [calculate_k(i, xa, ya) for i in range(len(xa))]

    for i in range(len(xa)):
        prod = product_of_combinations([xa[j] for j in range(len(xa)) if j != i])
        for j, val in enumerate(prod):
            polynomial[j] += ks[i] * val

    return make_it_nice(polynomial)
