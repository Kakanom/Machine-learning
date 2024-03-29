"""Модуль для визуализации данных"""

from matplotlib import pyplot as plt
import numpy as np


def draw_poly_class(x: np.array, y: np.array):
    """Визуализая клатеризации по 2 признакам

    На вход принимает:
        x - признаки
        y - метки классов

    Рисует график с классификацией данных
    """

    for i in range(len(np.unique(y))):
        xi = x[y == i]

        plt.plot(xi[:, 0], xi[:, 1], 'o', label=str(i))
    plt.legend()


def draw_lin(x: np.array, y: np.array, w: np.array):
    """Визуализая линейной регрессии по 2 признакам

    На вход принимает:
        x - признак(один, т.к. всего 2 веса)
        y - значения
        w - веса(длина = 2)

    Рисует получившуюся линейную регрессии

    Если длина массива весов не равна 2, то возвращается None
    """

    if len(w) != 2:
        return None

    def f(x):
        return w[0] + w[1] * x

    plt.plot(x, y, 'bo', x, f(x))


def draw_funcs(f_str: list, x_start: int, x_end: int, x_num: int, color=None):
    """Визуализация для данных двумерных функций.

    На вход принимает:
        f_str - список функций в виде строк
        x_start, x_end - отрезок, на котором отображаются функции
        x_num - количество точек для каждой функции
        color - Не обязательный параметр, содержит цвета для функций(в соответствии с обозначениями в matplotlib)

    Рисует данные функции на данном отрезке
    """

    x = np.linspace(x_start, x_end, x_num)
    y = []
    plot_str = 'plt.plot( '

    if color is None:
        for i in range(len(f_str)):
            y.append(eval(f_str[i]))
            plot_str += f'x, y[{i}], '
    else:

        for i in range(len(f_str)):
            y.append(eval(f_str[i]))
            plot_str += f'x, y[{i}], "{color[i]}", '

    plot_str = plot_str[0:len(plot_str)-2] + ')'

    eval(plot_str)
    plt.legend(f_str)
