from polynomial import Polynomial, make_it_nice, product_of_combinations

'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Полином Ньютона
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


def separated_differences(xa: list, ya: list, i: int = 1) -> list:
    result = [(ya[j] - ya[j + 1])/(xa[j] - xa[j + i]) for j in range(0, len(ya) - 1)]

    return [result[0]] + separated_differences(xa, result, i+1) if i != (len(xa) - 1) else [result[0]]


def newton_polynomial(xa: list, ya: list) -> Polynomial:
    polynomial = [0] * len(xa)
    polynomial[len(xa) - 1] += ya[0]

    sd = separated_differences(xa, ya)

    sd = make_it_nice(sd)

    for i in range(1, len(xa)):
        prod = product_of_combinations([xa[j] for j in range(i)])
        for j, val in enumerate(prod):
            polynomial[len(polynomial) - len(prod) + j] += val * sd[i - 1]

    return make_it_nice(polynomial)
