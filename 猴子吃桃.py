#CODING:UTF-8
import os
p=1
print("第10天剩余",p,"个桃子")
for i in range(9,0,-1):
    p = (p+1)*2
    print("第",i,"天剩余",p,"个桃子")
print("第一天总共有",p,"个桃子")
os.system("pause")
