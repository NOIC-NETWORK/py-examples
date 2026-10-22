#CODING:UTF-8
import os
a = eval(input("请输入数a:"))
b = eval(input("请输入数b:"))
c = eval(input("请输入数c:"))
if a > b:
    max_num = a
else:
    max_num = b
if max_num < c:
    max_num = c
print(max_num) 
os.system("pause")
