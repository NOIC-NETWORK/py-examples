#CODING:UTF-8
import os
def split_s(string, sep="", num=0):
    split_words = []
    last_index = 0
    count = 0
    for index, char in enumerate(string):
        if count == num and num > 0:
            split_words.append(string[last_index:len(string)])
            break
        if char == sep:
            split_words.append(string[last_index:index])
            last_index = index + 1
            count += 1
        elif index + 1 == len(string):
            split_words.append(string[last_index:index + 1])
    return split_words

print(split_s("life-is-short-you-need-python",'-'))
print(split_s("life-is-short-you-need-python",'-',2))
os.system("pause")
