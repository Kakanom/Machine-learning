"""Модуль для преообработки данных"""
import numpy as np

def np_cat(ar):
    """Преобразование категориальных признаков к числовым"""
    un = sorted(np.unique(ar))
    def my_map(elem):
        return un.index(elem)

    return np.vectorize(my_map)(ar)