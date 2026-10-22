#CODING:UTF-8
import os
for i in range(100,1000,1):
    i1 = i//100
    i2 = i//10%10
    i3 = i%10
    if i1**3+i2**3+i3**3==i:
        print(i,"为水仙花数")
os.system("pause")
