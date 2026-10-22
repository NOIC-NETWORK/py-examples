#CODING:UTF-8
import os
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)
a = int(input("请输入斐波那契数列的第x项:"))
print(fib(a))
os.system("pause")
