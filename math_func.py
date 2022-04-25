"""Модуль для математических функций"""

import numpy as np

def DerivativeInDots(f, x : np.array, eps = 1e-10):
    """Возвращает примерное значение производных в точках, поданных в массиве x"""
    return (f(x + eps) - f(x)) / eps

def LenOfVector(x : np.array):
    return  np.sqrt((x ** 2).sum())

def FindAngleBetweenVectors(vector_a, vector_b):
    """Возвращает угол в радианах между двумя векторами"""
    scalar_product = (vector_b * vector_a).sum()

    return np.arccos(scalar_product / (LenOfVector(vector_a) * LenOfVector(vector_b)))


def FindAngleBetweenPlanes(p1 : np.array, p2 : np.array):
    """"На вход принимает два массива вида: |xa yb zc ...|(константа опускается)
        Возвращает угол между плоскостями."""

    return np.arccos(abs(p1 * p2) / ((p1 ** 2).sum() * (p2 ** 2).sum()))




if __name__=='__main__':
    print('Вызов', __name__)
