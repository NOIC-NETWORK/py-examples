#CODING:UTF-8
import os
y = int(input("请输入年:"))
m = int(input("请输入月:"))
d = int(input("请输入日:"))
dl = [31,29,31,30,31,30,31,31,30,31,30,31]
cd = d
if y%4==0 and y%100!=0 or y%400==0:
    print(y,"年是闰年")
    dl[1] = 29
else:
    print(y,"年是平年")
    dl[1]=28
for i in range(m-1):
    cd+=dl[i]
print(y,"年",m,"月",d,"日是当年的",cd,"天")
os.system("pause")
