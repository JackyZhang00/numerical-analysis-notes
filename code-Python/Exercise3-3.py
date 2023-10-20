# 使用Legendre多项式进行三次拟合 Exercise3-3.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# 示例数据
x = np.array([3.73,5.63,8.67,10.49,13.26,16.74,19.55,22.19,25.36,28.31,30.83])
y = np.array([21.53,21.43,21.43,21.33,21.22,20.71,20.20,19.69,18.78,17.76,16.84])

# 进行Legendre拟合
coefficients = np.polynomial.legendre.legfit(x, y, 3)

# 绘制拟合曲线
x_fit = np.arange(3.73,30.83,0.01)
y_fit = np.polynomial.legendre.legval(x_fit, coefficients)
plt.scatter(x,y)
plt.plot(x_fit,y_fit,c="red")
plt.show()
