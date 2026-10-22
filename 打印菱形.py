#CODING:UTF-8
import os
def diamond(n):
    stack = []
    for i in range(1, 2 * n):
        if i <= n:
            p_str = ' ' * (n - i) + '*' * (2 * i - 1)
            if i != n:
                stack.append(p_str)
            print(p_str)
        else:
            print(stack.pop())
a = int(input("请输入菱形的高度:"))
diamond(a)
os.system("pause")
