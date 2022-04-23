""" Модуль для математических функций """
import numpy as np
def DerivativeInDots(f, x : np.array, eps = 1e-10):
    """Возвращает примерное значение производных в точках, поданных в массиве x"""
    return (f(x + eps) - f(x)) / eps

if __name__=='__main__':
    print('Вызов', __name__)
