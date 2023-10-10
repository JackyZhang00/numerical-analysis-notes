# 分段线性插值演示 Exercise2-4.py

import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return np.sin(x)

# 生成插值节点
n = 6
x = np.linspace(0, 2*np.pi, n)
y = f(x)

# 生成分段线性插值函数
x_interp = np.linspace(0, 2*np.pi, 1000)
y_interp = np.zeros_like(x_interp)
for i in range(len(x_interp)):
    if x_interp[i] <= x[0]:
        y_interp[i] = y[0]
    elif x_interp[i] >= x[-1]:
        y_interp[i] = y[-1]
    else:
        j = np.searchsorted(x, x_interp[i])
        x_left = x[j-1]
        x_right = x[j]
        y_left = y[j-1]
        y_right = y[j]
        slope = (y_right - y_left) / (x_right - x_left)
        y_interp[i] = y_left + slope * (x_interp[i] - x_left)

# 绘图
plt.plot(x_interp, f(x_interp))
plt.plot(x_interp, y_interp)
plt.plot(x, y, 'o')
plt.show()
