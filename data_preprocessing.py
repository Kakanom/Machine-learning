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

def StandartScaler(X):
    """Принимает на вход X - признаки объектов.
    Возвращает нормализованные признаки"""
    mean = X - np.mean(X)
    return mean / np.std(X)

if __name__=='__main__':
    print('Вызов',__name__)