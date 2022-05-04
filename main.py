# Импортируем библиотеку самописных математических функций import libs
from math_func import *
from visualization import *
from data_preprocessing import *
import numpy as np

# draw_funcs(["x", "x ** 2", "x ** 3 + 2"], -10, 10, 100, color = ["g", "y", "b"])
#
# plt.show()

# draw_funcs(['x', 'x ** 2', 'np.sin(x)', '1 / (1 + np.exp(-x))'], -2 * np.pi, 2 * np.pi, 10000)
#
# plt.show()


print(func_segment(fib, 1, 46, 1))
#
# draw_poly_class(X, Y)
#
# plt.show()