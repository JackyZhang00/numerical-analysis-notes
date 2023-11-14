# 使用紧凑格式的Doolittle三角分解法求解线性方程组 Exercise5-2.py

import numpy as np

def doolittle_triangular_decomposition(A):
    """
    Doolittle三角分解法
    """
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n)) 
    for i in range(n):
        L[i, i] = 1
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
            if i != j:
                L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
    return L, U

def forward_substitution(L, b):
    """
    前向替代
    """
    n = L.shape[0]
    x = np.zeros(n) 
    for i in range(n):
        x[i] = b[i] / L[i, i]
        for j in range(i):
            x[i] -= x[j] * L[i, j] / L[i, i]
    return x

def backward_substitution(U, b):
    """
    回代
    """
    n = U.shape[0]
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(U[i, j] * x[j] for j in range(i+1, n))) / U[i, i]
    return x

def doolittle_solver(A, b):
    """
    使用Doolittle三角分解法求解线性方程组
    """
    L, U = doolittle_triangular_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

A = np.array([[1,2,3],[2,5,2],[3,1,5]], dtype=float)
b = np.array([14,18,20], dtype=float)
x = doolittle_solver(A, b)
print("x=", x)