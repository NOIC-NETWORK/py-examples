#CODING:UTF-8
import os
def factor_sum(n):
    s_sum = 0
    for i in range(1, n):
        if n % i == 0:
            s_sum += i
    return s_sum

for j in range(1, 1000):
    if j == factor_sum(j):
        print(j)
os.system("pause")
