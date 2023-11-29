import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,-1,2])
y=np.array([0,3,4])

plt.scatter(x,y)

x=np.arange(-1,2,0.01)
y=-1.5*(x-1)+(11/6)*(x-1)*(x+1)
yd=3-1.5*(x+1)+(5/4)*(x+1)*(x-1)+(7/12)*(x+1)*(x-1)**2
yline=(x-1)
plt.plot(x,y)
plt.plot(x,yd)

plt.show()