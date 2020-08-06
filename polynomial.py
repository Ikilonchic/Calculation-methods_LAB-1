from colorama import Fore as fr
from itertools import combinations


'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Полином
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


Polynomial = list


def point_in_polynomial(polynomial: Polynomial, x: float) -> float:
    return sum([x**(len(polynomial) - i - 1) * coe for i, coe in enumerate(polynomial)])


def values(polynomial: Polynomial, xs: list) -> list:
    return [point_in_polynomial(polynomial, i) for i in xs]


def print_polynomial(polynomial: Polynomial) -> None:
    print(fr.BLUE, end='')
    length = len(polynomial)
    zero = True

    for i, elem in enumerate(polynomial):
        if elem != 0:
            if elem > 0 and not zero:
                print(' + ', end='')

            elif elem < 0:
                print(' - ', end='')

            if abs(elem) != 1 and i != length - 1:
                print(str(abs(elem)) + '*', end='')
                zero = False

            if i != length - 1:
                print('x', end='')

                if i < length - 2:
                    print('^' + str(length - i - 1) + ' ', end='')

                else:
                    print(' ', end='')

            else:
                print(abs(elem), end='')
                zero = False

        else:
            zero = True

    print(fr.RESET)


def make_it_nice(inp: Polynomial) -> Polynomial:

    inp = [round(elem, 8) for elem in inp]

    for i in range(len(inp)):
        if inp[i] == -0.0:
            inp[i] = 0.0

    return inp


def degree(inp: Polynomial) -> float:
    temp = len(inp) - 1
    
    while inp[temp] == 0.0:
        temp -= 1

    return temp


def product_of_combinations(inp: list) -> list:
    ls = [[j for j in combinations(inp, i)] for i in range(len(inp))]

    return [sum([product(s) for s in sub]) for sub in ls] + [product(inp)]


def product(ls: tuple) -> float:
    a = 1

    for elem in ls:
        a *= - elem

    return a
