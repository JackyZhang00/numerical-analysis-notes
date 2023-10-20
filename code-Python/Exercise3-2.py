# 演示线性拟合的最小二乘法 Exercise3-2.py

import numpy as np
import matplotlib.pyplot as plt

# 数据
x = np.array([0,20,40,60,80,100])
y = np.array([81.4,77.7,74.2,72.4,70.3,68.8])

# 进行线性拟合
coefficients = np.polyfit(x, y, 1)
slope = coefficients[0]
intercept = coefficients[1]

# 绘制拟合曲线
x_fit = np.arange(0,100,0.01)
y_fit = slope*x_fit+intercept
plt.scatter(x,y)
plt.plot(x_fit,y_fit,c="red")
plt.show()

# 打印拟合结果
print(f"表达式为{slope:.1f}t+{intercept:.1f}")
