#CODING:UTF-8
import os
for i in range(1000,10000,1):
    i1 = i//1000
    i2 = i//100%10
    i3 = i//10%10
    i4 = 1%10
    if i1**4 + i2**4 + i3**4 + i4**4==i:
        print(i,"是四叶玫瑰数")
os.system("pause")
