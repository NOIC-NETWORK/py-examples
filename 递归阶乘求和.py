#CODING:UTF-8
import os
def factor(n):
    if n < 2:
        return 1
    return n * factor(n - 1)

s_sum = 0
for i in range(1, 11):
    s_sum += factor(i)
print(s_sum)  
os.system("pause")
