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

# another metrics


if __name__ == '__main__':
    print('Вызов', __name__)
