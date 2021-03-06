"""Модуль для математических функций"""

import numpy as np

# Vectors and planes


def derivative_in_dots(f, x: np.array, eps=1e-10):
    """Возвращает примерное значение производных в точках, поданных в массиве x"""
    return (f(x + eps) - f(x)) / eps


def len_of_vector(x: np.array):
    return np.sqrt((x ** 2).sum())


def find_angle_between_vectors(vector_a: np.array, vector_b: np.array):
    """Возвращает угол в радианах между двумя векторами"""
    scalar_product = (vector_b * vector_a).sum()

    return np.arccos(scalar_product / (len_of_vector(vector_a) * len_of_vector(vector_b)))


def find_angle_between_planes(p1: np.array, p2: np.array):
    """"На вход принимает два массива вида: |xa yb zc ...|(константа опускается)
        Возвращает угол между плоскостями"""

    return np.arccos(abs(p1 * p2) / ((p1 ** 2).sum() * (p2 ** 2).sum()))


def manh(x, y):
    """На вход получает два вектора x и y, возвращает число, соответствующее манхэттенскому расстоянию между ними."""
    return abs(x - y).sum(axis=0)


# another functions

def fib(n):
    """Принимает на вход неотрицательное число n. Возвращает число Фибоначчи, стоящее на n - ном месте в ряду, используя
    формулу Бине
    """

    phi = ((1 + 5 ** 0.5) / 2)

    return round(((phi ** n) - ((-phi) ** -n)) / 5 ** 0.5)


def func_segment(f, start: int, end: int, eps=1):
    """Принимает на вход функцию f, концы отрезка: a и b, на котором нужно ее посчитать.
    Первоначально параметр eps равен 1, если он будет задан, то функция будет посчитана с промежутком eps
    """

    f = np.vectorize(f)
    x = np.linspace(start, end, (end - start) // eps + 1)

    return f(x)


def func(f, x):
    """Принимает на вход функцию f, x - множество, на котором нужно ее посчитать.
    Возвращает значения функции на множетсве x
    """

    f = np.vectorize(f)
    return f(x)


def poly_equation(x: np.array):
    """Принимает на вход коэффициенты многочлена.
    Возвращает его корни, они могут быть комплексными
    """

    return np.poly1d(x).roots


def polinom(a: np.array, x: np.array):
    """Принимает на вход два массива a, x.
    a - коэффициенты многочлена.(левый элемент - нулевой, далее - первой степени и т.д.)
    x - массив значений, в которых нужно посчитать многочлен.
    """

    x = np.array([x]).T
    x = np.insert(np.cumprod(np.repeat(x, len(a) - 1, axis=1), axis=1),
            np.repeat(np.array([0]), len(x.T)), np.repeat(np.array([1]), len(x.T)),
            axis=1)
    return np.sum(x * a, axis=1)


if __name__ == '__main__':
    print('Вызов', __name__)
