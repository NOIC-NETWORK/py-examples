#CODING:UTF-8
import os
a = input("请输入一个字符串:")
def get_permutations(instr):
    if len(instr) == 0:
        return []
    elif len(instr) == 1:
        return [instr]
    else:
        for j in range(len(instr)-1):
            if list(instr)[j] == list(instr)[j+1]:
                return False
        perms = []
        for i in range(len(instr)):
            current_char = instr[i]
            remaining_chars = instr[:i] + instr[i+1:]
            for perm in get_permutations(remaining_chars):
                perms.append(current_char + perm)
        return perms
if get_permutations(a)!=False:
    print(get_permutations(a))
else:
    print("请输入不重复字符的字符串！")
os.system("pause")
