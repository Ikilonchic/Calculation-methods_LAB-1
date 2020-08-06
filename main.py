import numpy as np
import colorama as color

from polynomial import Polynomial, print_polynomial, point_in_polynomial, make_it_nice
import graph

from lagrange import lagrange_polynomial
from newton import newton_polynomial
from square import square_polynomial


'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Меню
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


def print_menu() -> None:
    commands = {
        "polynomial": "\t - установка полиномов;\n",
        "graph": "\t\t - выведение графиков;\n",
        "table": "\t\t - таблица значений;\n",
        "help": "\t\t - просмотрт всех команд;\n",
        "exit": "\t\t - выход из программы.\n"
    }

    print()

    for i in commands.keys():
        print((color.Fore.CYAN if i != "exit" else color.Fore.RED) + i + color.Fore.BLUE
              + commands[i] + color.Fore.RESET)


def dispenser(inp: str) -> list:
    if type(inp) is not str:
        raise ValueError

    array = list(inp.split())

    for i in range(len(array)):
        array[i] = float(array[i])

    return array


'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Мейн функция
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''


def main() -> None:
    xa = list()
    ya = list()

    length = int()

    lagrange = Polynomial()
    newton = Polynomial()
    square = Polynomial()

    print(color.Fore.CYAN + "\t\t\t\t\tЛабораторная работа №1")

    while True: 
        try:
            print(color.Fore.CYAN + "Введите значения Х (через пробел): " + color.Fore.RESET, end='')
            xa = dispenser(input())

            print(color.Fore.CYAN + "Введите значения Y (через пробел): " + color.Fore.RESET, end='')
            ya = dispenser(input())

            if len(xa) != len(ya):
                raise RuntimeError

            print(color.Fore.CYAN + "Введите значения M: " + color.Fore.RESET, end='')
            ma = int(input())

            if ma >= len(xa):
                raise ReferenceError

            lagrange = lagrange_polynomial(xa, ya)

            print(color.Fore.CYAN + "Полином Лагранжа: " + color.Fore.RESET, end='')
            print_polynomial(lagrange)

            newton = newton_polynomial(xa, ya)

            print(color.Fore.CYAN + "Полином Ньютона: " + color.Fore.RESET, end='')
            print_polynomial(newton)
            
            square = square_polynomial(xa, ya, ma)

            print(color.Fore.CYAN + f"Полином среднеквад. co степ {ma}: " + color.Fore.RESET, end='')
            print_polynomial(square)

            graph.display_graph(xa, ya, (lagrange, newton, square), ma)

        except ReferenceError:
            print(color.Fore.RED + "Значение m > n. Введите значения повторно." + color.Fore.RESET)

        except RuntimeError:
            print(color.Fore.RED + "Количество значений Х и Y не совпадает. Введите значения повторно." + color.Fore.RESET)

        except ValueError:
            print(color.Fore.RED + "Вы ввели неправильные значения Х или Y. Попробуйте снова." + color.Fore.RESET)

        except:
            print(color.Fore.RED + "Неизвестная ошибка." + color.Fore.RESET)


if __name__ == "__main__":
    main()
