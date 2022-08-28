"""Модуль для предобработки данных"""
import numpy as np
from sklearn.metrics.pairwise import nan_euclidean_distances


def np_cat(ar):
    """Преобразование категориальных признаков к числовым

    Принимает на вход массив строковых признаков

    Возвращает числовые признаки
    """
    un = sorted(np.unique(ar))

    def my_map(elem):
        return un.index(elem)

    return np.vectorize(my_map)(ar)


def standart_scaler(x):
    """Принимает на вход X - признаки объектов.
    Возвращает нормализованные признаки
    """
    m = x - np.mean(x)

    return m / np.std(x)


def min_max_norm(x):
    """Принимает на вход признаки x, нормализует их, переводя все значения признака в интервал (0, 1)"""
    return (x - x.min(axis=0)) / (x.max(axis=0) - x.min(axis=0))


def fill_nan(x):
    """
    Заполняет все nan-значения в нормализованном
    двумерном массиве X типа np.array, заменяя их на похожие значения.
    Возвращает полученный массив.
    """
    m = nan_euclidean_distances(x)

    ii, jj = np.where(np.isnan(x))

    for i, j in zip(ii, jj):
        idx_zero = (m[i, :] == 0)
        mask = ~idx_zero

        z = (1 / m[i, mask]).sum()

        s = np.nansum(x[mask, j] / (m[i, mask]))
        x[i, j] = s / z
    return x


if __name__ == '__main__':
    print('Вызов', __name__)
