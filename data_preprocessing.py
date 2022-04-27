"""Модуль для предобработки данных"""
import numpy as np

def np_cat(ar):
    """Преобразование категориальных признаков к числовым

    Принимает на вход массив строковых признаков

    Возвращает числовые признаки
    """
    un = sorted(np.unique(ar))
    def my_map(elem):
        return un.index(elem)

    return np.vectorize(my_map)(ar)

