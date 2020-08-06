import matplotlib.pyplot as plt
import pylab
import prettytable as pt
import colorama

from polynomial import make_it_nice, values, degree

def draw_graph(xa: list, ya: list, xs: list, *ys: tuple) -> None:
    plt.figure(figsize=(12, 7))
    plt.grid(True)

    plt.plot(xs, ys[0][0], 'r-', label=ys[0][1])
    plt.plot(xs, ys[1][0], 'go', label=ys[1][1])
    plt.plot(xs, ys[2][0], 'bo', label=ys[2][1])

    plt.plot(xa, ya, 'r^')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Графики полиномов")

    plt.show()


def print_table(xa: list, ya: list, xs: list, *ys: tuple) -> None:
    print(colorama.Fore.RESET, end = '')
    t = pt.PrettyTable([f"{colorama.Fore.RED}X{colorama.Fore.RESET}"] + [f"{colorama.Fore.GREEN}{y[1]}{colorama.Fore.RESET}" for y in ys])

    for i in range(len(xs)):
        t.add_row([f"{colorama.Fore.YELLOW}{xs[i]}{colorama.Fore.RESET}"] + [str(y[0][i]) for y in ys])

    print(t)


def display_graph(xa: list, ya: list, polynomials: tuple, ma) -> None:
    points = []
    temp = xa[0] - 1

    while temp < xa[-1] + 1:
        points += [round(temp, 4)]
        temp += 0.1

    #points += [round(xa[-1], 4)]

    lag = make_it_nice(values(polynomials[0], points))
    new = make_it_nice(values(polynomials[1], points))
    squ = make_it_nice(values(polynomials[2], points))

    draw_graph(xa, ya, points, (lag, "лагранж"), (new, "ньютон вперед"), (squ, f"средн.кв., m = {ma}"))
    print_table(xa, ya, points, (lag, "лагранж"), (new, "ньютон вперед"), (squ, f"средн.кв., m = {ma}"))
