#CODING:UTF-8
"""求函数f（x）的最小值
T0:         系统的初始温度（高温状态）
Tf:      温度的下限
rate:       控制降温的速率
f(now)：　　　   系统当前状态的评价函数值
f(new):　 　　系统新状态的评价函数值
===============伪代码===============
while (T0 > Tf)
{
    if f(new) - f(now) < 0
    　　f(now) = f(new)
    else if (exp(f(new) - f(now) / T0) > random(0,1))
    　　f(now) = f(new)
    else
    　　不更新f(now)
    T0 = T0 * rate;
    更新状态new        　　　　　　　　
}

循环结束，得到模拟退火求得的最小值f(now)
"""
import os
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
# define aim function
def aimFunction(x):
    y = x ** 3 - 60 * x ** 2 - 4 * x + 6
    return y


x = [i / 10 for i in range(1000)]
y = [0 for i in range(1000)]
for i in range(1000):
    y[i] = aimFunction(x[i])

plt.plot(x, y)
T = 1000  # initiate temperature
Tmin = 10  # minimum value of terperature
x = np.random.uniform(low=0, high=100)  # initiate x
k = 50  # times of internal circulation
y = 0  # initiate result
t = 0  # time
while T >= Tmin:
    for i in range(k):
        # calculate y
        y = aimFunction(x)
        # generate a new x in the neighboorhood of x by transform function
        xNew = x + np.random.uniform(low=-0.055, high=0.055) * T
        if (0 <= xNew and xNew <= 100):
            yNew = aimFunction(xNew)
            if yNew - y < 0:
                x = xNew
            else:
                # metropolis principle
                p = math.exp(-(yNew - y) / T)
                r = np.random.uniform(low=0, high=1)
                if r < p:
                    x = xNew
    t += 1
    print(t)
    T = 1000 / (1 + t)  #降温函数，也可使用T=0.9T
print(x, aimFunction(x))
os.system("pause")
