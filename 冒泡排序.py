#CODING:UTF-8
import os
import numpy
pl = numpy.random.randint(100,size=6)
c = len(pl)
print(pl)
for i in range(c-1):
    for j in range(c-i-1):
        if pl[j] > pl[j+1]:
            pl[j],pl[j+1]=pl[j+1],pl[j]
print(pl)
os.system("pause")
