# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:40:15 2018

@author: yison
"""
import sys

IN_FILE_PATH = 'D:/E_lerning/Spyder_workspace/words.txt'
OUT_FILE_PATH = 'D:/E_lerning/Spyder_workspace/Q1.txt'


def stat_words(in_path):
    res_word = []
    res_count = {}
    # stat appear time
    with open(in_path) as f:
        whole_txt = f.read()
        words = whole_txt.split(' ')
        #print (words)
        for word in words:
            if word in res_word:
                res_count[word] += 1
            else:  # first appear
                res_word.append(word)
                res_count[word] = 1

    # write to file
    file_object = open(OUT_FILE_PATH, 'w')
    print (len(res_word))
    for i in range(0, len(res_word)):
        file_object.write("%s %d %d\n" %(res_word[i], i, res_count[res_word[i]]))
    file_object.close()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        in_path = sys.argv[1]
    else:
        in_path = IN_FILE_PATH
    stat_words(in_path)