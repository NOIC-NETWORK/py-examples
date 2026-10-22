#CODING:UTF-8
import os
def valid_str(string):
    if len(string) % 2 == 1:
        return False
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()', '')
        string = string.replace('[]', '')
        string = string.replace('{}', '')
    return string == ''
a = input("请输入字符串:")
print(valid_str(a))
os.system("pause")
