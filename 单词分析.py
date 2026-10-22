#CODING:UTF-8
import os
def analyse_words(words):
    word_dict = {}
    for i in words:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    max_key = max(word_dict,key=word_dict.get)
    print(max_key)
    print(word_dict[max_key])
analyse_words('helloworld')
os.system("pause")
