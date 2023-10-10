# 三次样条插值演示(自然边界条件) Exercise2-6.py

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# 创建一些数据点
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 2, 1, 3, 2, 0])

# 使用CubicSpline函数进行样条插值
cs = CubicSpline(x, y)

# 生成插值点
x_interp = np.linspace(0, 5, 100)
y_interp = cs(x_interp)

# 绘制原始数据和插值曲线
plt.plot(x, y, 'o')
plt.plot(x_interp, y_interp)
plt.show()
