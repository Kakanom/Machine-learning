"""Модуль для математических функций"""

import numpy as np
import math

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


# Number Theory

def factorization(x):
    """На вход получает натуральное число.
    Возвращает два массива div и count - делители и их степени соответственно"""
    divs = []
    count = []

    i = 2
    while i * i <= x:
        c = 0
        while x % i == 0:
            c += 1
            x //= i
        if c > 0:
            divs.append(i)
            count.append(c)
        i += 1

    if x > 1:
        divs.append(x)
        count.append(1)

    return divs, count


def phi(n):
    """Принимает на вход натуральное число большее 2.
    Возвращает количество взаимнопростых с n чисел из отрезка [1, n]"""
    res = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            res -= res//p

        while n % p == 0:
            n //= p

        p += 1

    if n > 1:
        res -= res//n

    return res

# another functions

def bin_pow(x, n):
    """Принимает на вход числа x и n.
    Возвращает x^n"""
    res = 1
    while n:
        if n & 1:
            res *= x
            n -=1
        else:
            x *= x
            n >>= 1

    return res

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

# permutations etc


def permutations(n, k):
    """Возвращает перестановки из n по k"""
    return math.factorial(n) / math.factorial(n - k)


def C(n, k):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


def eratosthenes_sieve(self, n: int) -> int:
    """returns number of prime numbers from 0 to n - 1"""
    if n < 3:
        return 0

    sieve = [False, False] + [True] * (n - 2)

    for i in range(2, int(math.sqrt(n) + 1)):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False

    return sieve.count(True)


