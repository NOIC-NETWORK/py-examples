#CODING:UTF-8
import os
al = [5,7,11,22,27,33,39,52,58]
def bs(num,l,r):
    if l<=r:
        m = (l+r)//2
        if num<al[m]:
            r=m-1
        elif num>al[m]:
            l=m+1
        else:
            return m
        return bs(num,l,r)
    else:
        return -1
printf("%d",bs(11,0,len(al)-1))
os.system("pause")
