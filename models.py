"""Модуль, содержащий в себе некоторые модели машинного обучения"""
from visualization import *
from sklearn.metrics.pairwise import nan_euclidean_distances

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
    """Класс, реализующий линейную регрессию"""

    def __init__(self, learning_rate=0.005, iter=20000, eps=1e-10):
        """
        :param learning_rate: скорость обучения
        :param iter: количество итерация обучения
        :param eps: разница между значениями mse для остановки обучения
        """
        self.lr = learning_rate
        self.iter = iter
        self.eps = eps
        self.w = None
        self.log = None

    def fit(self, x: np.array, y: np.array):

        if x.shape[0] != y.shape[0]:
            raise ShapeError("У массивов разные размерности!")

        w = np.array([[1. for _ in range(len(x.T) + 1)]]).T
        x = np.insert(x, 0, 1, axis=1)

        yp = np.dot(x, w).sum(axis=1)
        mse = MSE(y, yp)

        self.log = np.array([w.copy()])

        for i in range(self.iter):

            w -= np.array([2 * self.lr * ((yp - y) * x.T).sum(axis=1)]).T / y.size

            yp_new = np.dot(x, w).sum(axis=1)
            mse_new = MSE(y, yp_new)

            if abs(mse - mse_new) < self.eps:
                break
            yp = yp_new
            mse = mse_new

            self.log = np.append(self.log, np.array([w]), axis = 0)

        self.w = w

    def get_lin(self, x):
        x = np.insert(x, 0, 1, axis=1)
        return np.dot(x, self.w)

    def predict(self, x):
        """Принимает на вход массив признаков.
        Возвращает предсказанные значения."""
        if self.w is None:
            raise FitError("Model hasn't been fitted yet")

        return self.get_lin(x)

    def score(self, x, y_true):
        y_pred = self.get_lin(x).T
        return MSE(y_true, y_pred)


class Kmeans:
    """Класс кластеризации алгоритмом k-средних"""

    def __init__(self, n_clusters, max_iter=100):
        """

        :param n_clusters:
        :param max_iter:
        """
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.centroids = None


    def find_labs(self, x, centroids):
        """классифицирует данные для текущих центроидов

        :param x: признаки объектов
        :param centroids: расположение центроидов
        :return: метки классов для объектов
        """
        dist = nan_euclidean_distances(x, centroids)
        return np.argmin(dist, axis = 1)


    def find_eucl_sum(self, x, point):
        return nan_euclidean_distances(x, [point]).sum(axis = 1)


    def find_centroids(self, x, labs):
      return np.array([x[labs == i].mean(axis = 0) for i in np.unique(labs)])


    def find_closest_cluster(self, distance):
        return np.argmin(distance, axis=1)


    def clusterize(self, x, eps = 1e-3, tries = 100):
        """кластеризует данные на n кластеров.

        :param x: признаки объектов
        :param eps: изминение расположения весов для того, чтобы остановить кластеризацию
        :param tries: количество попыток запуска(из-за случайной генерации может получиться так, что какой-то кластер
                                                                                                останется без объектов)
        :return: метки классов для данных объектов(возвращает None, если не удалось кластеризовать, возможно,
                                                                                                стоит запустить еще раз)

        если вам нужно определить метки для других объектов по уже обученной модели, то используйте метод find_labs,
        указав центроиды как instance_name.centroids
        """
        for i in range(tries):
            try:
                if self.n_clusters < 2:
                    return np.zeros((x.shape[0], 1))

                centroids = np.random.normal(loc=0.0, scale=5., size=self.n_clusters * x.shape[1]). \
                    reshape((self.n_clusters, x.shape[1]))

                labs = self.find_labs(x, centroids)

                centroids1 = self.find_centroids(x, labs)

                while abs(centroids - centroids1).max() > eps:
                    labs = self.find_labs(x, centroids1)

                    centroids = centroids1.copy()
                    centroids1 = self.find_centroids(x, labs)

                if len(np.unique(labs)) < self.n_clusters:
                    continue

                self.centroids = centroids1

                return labs

            except Exception:
                continue

        return None

    def quality_of_clustering(self, x, labs):
        """Метод, возвращающий качество кластеризации

        :param x: признаки объектов
        :param labs: их метки классов
        :return: качество кластеризации(усредненная сумма растояний до центров)
        """
        S = 0

        for i in np.unique(labs):
            S += (self.find_eucl_sum(x[labs == i], x[labs == i].mean(axis=0))).sum()

        return S


if __name__ == '__main__':
    print('Вызов', __name__)
