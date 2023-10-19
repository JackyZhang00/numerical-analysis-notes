# 使用Legendre多项式进行平方逼近演示(例题解答) Exercise3-1.py

import numpy as np
from scipy.special import legendre
from scipy.optimize import least_squares

# 计算Legendre多项式的系数
def legendre_coefficients(x, y, degree):
    A = np.zeros((len(x), degree + 1))
    for i in range(degree + 1):
        A[:, i] = legendre(i)(x)
    return np.linalg.lstsq(A, y, rcond=None)[0]

# 定义逼近函数
def approximation_func(x, coefficients):
    result = np.zeros_like(x)
    for i, coeff in enumerate(coefficients):
        result += coeff * legendre(i)(x)
    return result

def legendre_approximation(x, y, degree):
    # 计算逼近函数的系数
    coefficients = legendre_coefficients(x, y, degree)

    # 使用最小二乘法优化逼近函数的系数
    result = least_squares(lambda coefficients: approximation_func(x, coefficients) - y, coefficients)

    return result.x

# 示例数据
x = np.linspace(-1, 1, 100)
y = np.exp(x)

# 最佳平方逼近
degree = 3
coefficients = legendre_approximation(x, y, degree)

# 计算逼近函数的值
approximation = approximation_func(x, coefficients)

# 打印结果
print("系数:", coefficients)
