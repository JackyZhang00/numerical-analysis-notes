# 使用列主元Gauss消去法求解方程组 Exercise5-1.py

import numpy as np

#使用列主元Gauss消去法求解方程组
def gauss_elimination(A, b):
    n = A.shape[0]
    # 消元
    for j in range(n):
        # 选择最大值作为主元
        max_idx = j + np.argmax(np.abs(A[j:, j]))
        if j != max_idx:
            A[[j, max_idx]] = A[[max_idx, j]]
            b[[j, max_idx]] = b[[max_idx, j]]
        # 计算主元下面的元素
        pivot = A[j, j]
        for i in range(j+1, n):
            factor = A[i, j] / pivot
            A[i, :] -= factor * A[j, :]
            b[i] -= factor * b[j]
    # 回代
    x = np.zeros(n)
    for j in range(n-1, -1, -1):
        x[j] = (b[j] - np.dot(A[j, j+1:], x[j+1:])) / A[j, j]
    return x

# 计算方程组
A = np.array([[1,1,1],[2,2,-1],[3,0,1]], dtype=float)
b = np.array([6,3,6], dtype=float)
x = gauss_elimination(A, b)
print("x=", x)