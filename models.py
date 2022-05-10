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

    def __init__(self, learning_rate=0.005, iter=200, eps=1e-10):
        self.lr = learning_rate
        self.iter = iter
        self.w = None
        self.log = None
        self.eps = eps

    def fit(self, x: np.array, y: np.array):
        if x.shape[0] != y.shape[0]:
            raise ShapeError("У массивов разные размерности!")

        w = np.array([[1. for _ in range(len(x.T) + 1)]]).T

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
            if abs(mse - mse_new) < self.eps:
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


# class FOREL:
#     def __init__(self, x, r):
#         self.x = x
#         self.r = r
#         self.clusters = None
#
#     def find_centroid(self, x, c):
#         """
#         Принимает на вход список объектов x и список столбцов c, по которым ищется
#         центр тяжести. Возвращает центр тяжести
#         """
#
#         return x[c].mean(axis=0)
#
#     def find_cluster(self, x, f):
#         """
#         f - координаты случайной точки
#         """
#
#         c = [i for i in range(x.shape[0]) if nan_euclidean_distances([X[i, :]], [f]) <= R]
#         f = self.find_centroid(x, c)
#         c1 = [i for i in range(x.shape[0]) if nan_euclidean_distances([X[i, :]], [f]) <= R]
#         while c != c1:
#             f = self.find_centroid(x, c)
#             c = c1
#             c1 = [i for i in range(x.shape[0]) if nan_euclidean_distances([X[i, :]], [f]) <= R]
#
#         return c
#
#     def find_all_clusters(self):
#         cl = []
#         iter = 0
#         while self.x.shape[0] > 0 and iter < 10:
#             f = np.random.randint(self.x.max(), size=2)
#             cl += [self.find_cluster(x, self.r, f)]
#             x = np.delete(x, cl, axis=0)
#             iter += 1
#
#         return cl
#
#     def fit(self):
#         self.clusters = self.find_all_clusters()
#
#     def visualization(self):
#         draw_poly_class(self.x, self.clusters)


# class Kmeans:
#     """Класс кластеризации алгоритмом k средних"""
#
#     def __init__(self, n_clusters, max_iter=100):
#         self.n_clusters = n_clusters
#         self.max_iter = max_iter
#
#
#     def find_labs(self, x, centroids):
#         dist = nan_euclidean_distances(x, centroids)
#         return np.argmin(dist, axis = 1)
#
#
#     def find_eucl_sum(self, x, point):
#         return nan_euclidean_distances(x, [point]).sum(axis = 1)
#
#
#     def find_centroids(self, x, labs):
#       return np.array([x[labs == i].mean(axis = 0) for i in np.unique(labs)])
#
#
#     def find_closest_cluster(self, distance):
#         return np.argmin(distance, axis=1)
#
#
#     def fit(self, x, k):
#         if k < 2: return np.zeros((x.shape[0], 1))
#
#         centroids = np.random.normal(loc=0.0, scale=5., size=k * X.shape[1]). \
#             reshape((k, x.shape[1]))
#
#
#         labs = self.find_labs(x, centroids)
#
#         centroids1 = self.find_centroids(x, labs)
#
#         while abs(centroids - centroids1).max() > 1e-2:
#             labs = self.find_labs(x, centroids1)
#
#             centroids = centroids1.copy()
#             centroids1 = self.find_centroids(x, labs)
#
#         return labs
#
#     def predict(self, x):


# class LinearReg:
#     """Класс линейной регрессии"""
#     def __init__(self, learning_rate=1e-3, n_steps=1000):
#         self.learning_rate = learning_rate
#         self.n_steps = n_steps
#
#     def fit(self, X, Y):
#         '''
#         Method for learning the optimal parameters of the model
#         '''
#
#         # adding the bias term
#         Xtrain = np.c_[np.ones(X.shape[0]), X]
#
#         # random initialization of the model weights
#         self.W = np.random.rand((Xtrain.shape[1]))
#
#         # iteratively updating W for n_steps
#         for i in range(self.n_steps):
#             self.W = self.W - self.learning_rate * self.calcGradient(Xtrain, Y)
#
#     def predict(self, X):
#         '''
#         Predicting Y for the X
#         '''
#
#         # adding the bias term
#         Xpred = np.c_[np.ones(X.shape[0]), X]
#
#         return np.dot(Xpred, self.W)
#
#     def calcGradient(self, X, Y):
#         '''
#         Implementation of the gradient of the Loss function
#         '''
#         return 2 / X.shape[0] * np.dot(X.T, (np.dot(X, self.W) - Y))


if __name__ == '__main__':
    print('Вызов', __name__)
