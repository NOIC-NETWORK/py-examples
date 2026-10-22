#CODING:UTF-8
import os
import random as r
a = r.randint(1,100)
i=1
while True:
    an = int(input("请输入数字:"))
    if an==a:
        print("答对了,答题次数",i,"次")
        break
    elif an>a:
        print("过大！")
        i+=1
    elif an<a:
        print("过小！")
        i+=1
os.system("pause")
