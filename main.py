# Импортируем библиотеку самописных математических функций import libs
from math_func import *
from visualization import *
from data_preprocessing import *
import numpy as np

draw_funcs(["x", "x ** 2", "x ** 3 + 2"], -2, 2, 100, color = ["g", "y", "b"])

plt.show()