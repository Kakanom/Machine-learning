# Импортируем библиотеку самописных математических функций import libs
from math_func import *
from visualization import *
from data_preprocessing import *
import numpy as np

# draw_funcs(["x", "x ** 2", "x ** 3 + 2"], -10, 10, 100, color = ["g", "y", "b"])
#
# plt.show()

def func(x):
    return x ** 2

print(func_segment(func, 1, 4, 4))
print(np.linspace(1, 3, 1))

# print(np.linspace.__doc__)