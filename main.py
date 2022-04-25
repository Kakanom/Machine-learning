# Импортируем библиотеку самописных математических функций
from math_func import *
import numpy as np




# print(math_func.DerivativeInDots(lambda x: x ** 2, np.array(1)))

print(LenOfVector(np.array([1, 2, 3])))

print(FindAngleBetweenVectors(np.array([1, 0, 0]), np.array([1, 2, 3])))