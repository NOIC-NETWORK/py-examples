#CODING:UTF-8
import os
def is_palindrome(x):
    if x < 0 or x > 0 and x % 10 == 0:
        return False
    str_x = str(x)
    return str_x == str_x[::-1]
a = int(input("请输入数:"))
print(is_palindrome(a))  
os.system("pause")
