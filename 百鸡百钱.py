#CODING:UTF-8
import os
c = 0
for x in range(1,20,1):
    for y in range(1,33,1):
        z = 100-x-y
        if z>0 and 5*x+3*y+z/3==100:
            c+=1
            print("第",c,"种买法,公鸡",x,"只,母鸡",y,"只，小鸡",z,"只")
os.system("pause")
