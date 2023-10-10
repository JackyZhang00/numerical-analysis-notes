# Runge现象演示 Exercise2-3.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

# 定义函数
def f(x):
    return 1 / (1 + x ** 2)

# 生成插值节点
n = 11
x = np.linspace(-5, 5, n)
y = f(x)

# 生成插值多项式
poly = lagrange(x, y)

# 生成等距节点
x_interp = np.linspace(-5, 5, 1000)
y_interp = f(x_interp)

# 生成插值函数
y_poly = poly(x_interp)

# 绘图
plt.plot(x_interp, y_interp)
plt.plot(x_interp, y_poly)
plt.plot(x, y, 'o')
plt.show()
