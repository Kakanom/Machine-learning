"""Модуль, содержащий в себе метрики машинного обучения"""
import numpy as np

# linear model metrics


def rmse(y_r: np.array, y_pr: np.array):
    """Принимает на вход y_r, y_pr - правильные значения и предсказанные соответственно.
    Возвращает среднюю квадратичную ошибку"""
    return np.sqrt(((y_r - y_pr) ** 2).mean())


def mae(y_r: np.array, y_pr: np.array):
    """Принимает на вход y_r, y_pr - правильные значения и предсказанные соответственно.
    Возвращает среднюю абсолютную ошибку"""
    return (abs(y_r - y_pr)).mean()

# classification metrics


def accuracy(y: np.array, yp: np.array):
    """Принимает на вход правильные метки(y) и предсказанные(yp).
    Возвращает процент правильных предсказаний в отрезке [0, 1]"""

    return (y == yp).sum() / len(y)


def precision(y: np.array, yp: np.array):
    """Принимает на вход правильные метки(y) и предсказанные(yp).
    Возвращает точность предсказаний"""

    TP = np.all(np.array([y == yp, y == 1]), axis=0).sum()
    FP = np.all(np.array([y == 0, yp == 1]), axis=0).sum()

    print(TP, FP)

    return TP / (TP + FP)


def recall(y: np.array, yp: np.array):
    """Принимает на вход правильные метки(y) и предсказанные(yp).
    Возвращает полноту предсказаний"""

    TP = np.all(np.array([y == yp, y == 1]), axis=0).sum()
    FN = np.all(np.array([yp == 0, y == 1]), axis=0).sum()

    return TP / (TP + FN)


def F(y: np.array, yp: np.array):
    """Принимает на вход правильные метки(y) и предсказанные(yp).
    Возвращает полноту предсказаний"""

    pr = precision(y, yp)
    rec = recall(y, yp)

    return 2 * pr * rec / (pr + rec)
