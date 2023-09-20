# 演示大数"吃"小数

import numpy as np

# 使用从左到右的计算方式, 会有很大误差
def example1():
    result = np.float32(0)
    result = result + np.float32(1e9)
    for i in range(1,41):
        result = result + np.float32(i)
    print(f"从左到右计算结果为{result}")

# 使用从右到左的计算方式, 误差较小
def example2():
    result = np.float32(0)
    for i in range(1,41):
        result = result + np.float32(i)
    result = result + np.float32(1e9)
    print(f"从右到左计算结果为{result}")

example1()
example2()