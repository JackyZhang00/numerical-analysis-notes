# 分段三次Hermite插值演示 Exercise2-5.py

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.interpolate import PchipInterpolator 

# 定义函数 
def f(x): 
   return np.sin(x)
 
# 生成插值节点 
n = 5 
x = np.linspace(0, 2*np.pi, n)
y = f(x)

# 生成分段三次Hermite插值函数 
x_interp = np.linspace(0, 2*np.pi, 1000)
y_interp = PchipInterpolator(x, y)(x_interp)
 
# 绘图 
plt.plot(x_interp, f(x_interp)) 
plt.plot(x_interp, y_interp) 
plt.plot(x, y, 'o') 
plt.show()