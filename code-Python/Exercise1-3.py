# 演示100000次多项式不同算法时间差异(假设每一项系数a_n都是2)

import time
POWER = 100000
# 直接求和
def method1():
    result = 0
    x = 2
    a = []
    for i in range(0,POWER+1):
        a.append(2)
    start_time = time.time()
    for i in range(0,POWER+1):
        result = result + a[i]*x**i
    end_time = time.time()
    # print(result)
    print(end_time-start_time)

# 使用逐项求和
def method2():
    result = 0
    x = [1,2]
    for i in range(2,POWER+1):
        x.append(x[i-1]*2)
    a = []
    for i in range(0,POWER+1):
        a.append(2)
    start_time = time.time()
    for i in range(0,POWER+1):
        result = result + a[i]*x[i]
    end_time = time.time()
    # print(result)
    print(end_time-start_time)

# 秦九韶算法
def method3():
    s = 2
    x = 2
    start_time = time.time()
    for i in range(1,POWER+1):
        s = s*x+2
        # s.append(s[i-1]*x+2)
    end_time = time.time()
    # print(s)
    print(end_time-start_time)

method1()
method2()
method3()