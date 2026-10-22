#CDOING:UTF-8
import os
for x in range(1,101,1):
    if x % 2 == 0: 
        a = int((x ** 2) / 2)
    else: 
        a = int((x ** 2 - 1) / 2)
    print(a)
os.system("pause")
