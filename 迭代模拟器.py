#CODING:UTF-8
import os
def p(n):
    if n == 0:
        return
    print('递归前->',n)
    p(n-1)
    print('递归后->',n)
a = int(input("请输入迭代次数:"))
p(a)
os.system("pause")
