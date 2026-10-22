#CODING:UTF-8
import os
def sum_square(n):
    sum = 0
    for i in str(n):
        sum += int(i) ** 2
    return sum

list1 = []
n = int(input('请输入数字：'))
while sum_square(n) not in list1:
    n = sum_square(n)
    list1.append(n)

if n == 1:
    print('是快乐数')
else:
    print('不是快乐数')

os.system("pause")
