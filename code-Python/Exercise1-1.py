# 验证数值稳定性(例题)

## 方法1(数值不稳定)

def I1(n):
    if n==0:
        return 0.182
    else:
        return 1/n-5*I1(n-1)
    
def I2(n):
    if n==9:
        return 0.017
    else:
        return 1/(5*(n+1))-(1/5)*I2(n+1)

for n in range(0,9):
    print(f"I1_{n} = {I1(n)}")

for n in range(0,9):
    print(f"I2_{n} = {I2(n)}")