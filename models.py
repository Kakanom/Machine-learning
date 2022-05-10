"""Модуль, содержащий в себе некоторые модели машинного обучения"""
from visualization import *


# linear regression


def MSE(y, yp):
    return np.sum((y-yp)**2)/y.size


class ShapeError(Exception):
    def __init__(self, text):
        self.txt = text


class FitError(Exception):
    def __init__(self, text):
        self.txt = text


class LinReg:

    def __init__(self, learning_rate=0.005, iter=200):
        self.lr = learning_rate
        self.iter = iter
        self.w = None
        self.log = None

    def fit(self, x: np.array, y: np.array):
        if x.shape[0] != y.shape[0]:
            raise ShapeError("У массивов разные размерности!")

        w = np.array([[1. for i in range(len(x.T) + 1)]]).T

        self.log = w.copy()

        x = np.insert(x, 0, 0, axis=1)

        yp = np.dot(x, w).sum(axis=1)
        mse = MSE(y, yp)

        for i in range(self.iter):

            # шаг для каждого из весов - здесь была ошибка

            w[0] -= 2 * self.lr * np.sum(yp - y)/y.size
            w[1:] -= np.array([2 * self.lr * ((yp - y) * x.T).sum(axis=1)[1:]]).T / y.size

            yp_new = np.dot(x, w).sum(axis=1)
            mse_new = MSE(y, yp_new)

            # Критерий остановки обучения - разница между значениями MSE меньше, чем 0.01
            # Вычтем из старого значения MSE новое, полученное уже после обновления весов.
            if abs(mse - mse_new) < 0.0001:
                break
            yp = yp_new
            mse = mse_new

            self.log = np.append(self.log, w)

        self.w = w

    def get_lin(self, x):
        x = np.insert(x, 0, 0, axis=1)
        return np.dot(x, self.w) + self.w[0]

    def predict(self, x):
        """Принимает на вход массив признаков.
        Возвращает предсказанные значения."""
        if self.w is None:
            raise FitError("Model hasn't been fitted yet")

        return self.get_lin(x)

    def score(self, x, y_true):
        y_pred = self.get_lin(x).T
        return MSE(y_true, y_pred)


if __name__ == '__main__':
    print('Вызов', __name__)
