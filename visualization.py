"""Модуль для визуализации данных"""
from matplotlib import pyplot as plt
import numpy as np

def draw_poly_class(X, Y):
    """Визуализая клатеризации по 2 признакам"""
    for i in range(len(np.unique(Y))):
        x = X[Y == i]

    plt.plot(x[:, 0], x[:, 1], 'o', label = str(i))
    plt.legend()

if __name__=='__main__':
    print('Вызов',__name__)