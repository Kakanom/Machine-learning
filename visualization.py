"""Модуль для визуализации данных"""

from matplotlib import pyplot as plt
from matplotlib import animation as ani
from IPython.display import HTML
import numpy as np

def draw_poly_class(X, Y):
    """Визуализая клатеризации по 2 признакам

    На вход принимает:
        X - признаки
        Y - метки классов

    Рисует график с классификацией данных
    """
    for i in range(len(np.unique(Y))):
        x = X[Y == i]

    plt.plot(x[:, 0], x[:, 1], 'o', label = str(i))
    plt.legend()

def draw_funcs(f_str : list, x_start : int, x_end : int, x_num : int, color : list):
    """Визуализация для данных двумерных функций.

    На вход принимает:
        f_str - список функций в виде строк
        x_start, x_end - отрезок, на котором отображаются функции
        x_num - количество точек для каждой функции
        color - цвета для функций(в соответствии с обозначениями в matplotlib)

    Функция возвращает None, рисует данные функции на данном отрезке
    """

    x = np.linspace(x_start, x_end, x_num)
    y = []
    plot_str = 'plt.plot( '

    for i in range(len(f_str)):
      y.append(eval(f_str[i]))
      plot_str += f'x, y[{i}], "{color[i]}", '

    plot_str = plot_str [0:len(plot_str)-2] + ')'

    eval(plot_str)
    plt.legend(f_str)


if __name__=='__main__':
    print('Вызов',__name__)

