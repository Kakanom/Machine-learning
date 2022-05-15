from models import *
from sklearn.datasets import make_blobs
import numpy as np

def draw_funcs_ex1():
    draw_funcs(["x", "x ** 2", "x ** 3 + 2"], -10, 10, 100)

    plt.show()
def draw_funcs_ex2():
    draw_funcs(['x', 'x ** 2', 'np.sin(x)', '1 / (1 + np.exp(-x))'], -2 * np.pi, 2 * np.pi, 10000)

    plt.show()

def linreg_ex():
    x = np.array([np.arange(0.0, 6.0, 0.5)]).T
    y = np.array([ 7.32808219,  8.88210587,  8.92239811, 10.52462399, 12.91597313,
                12.55843474, 14.81755614, 18.31825374, 19.44109095, 18.76040251,
                20.07294082, 22.10215284])

    mod = LinReg()
    mod.fit(x, y)

    draw_lin(x, y, mod.w)

    plt.show()


def kmeans_ex(n_centroids = 2):
    X, labs = make_blobs(1000, centers=n_centroids)

    mod = Kmeans(n_clusters=n_centroids)
    lab = mod.clusterize(X)

    draw_poly_class(X, lab)
    plt.show()