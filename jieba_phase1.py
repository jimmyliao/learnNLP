# -*- coding: utf-8 -*-
# Author：jimmyliao
# Date: 2016-06-15
#encoding=utf-8
import jieba

# jieba.set_dictionary('dict.txt.big')

content = open('./input/input1.txt', 'rb').read()

# print("Input：", content)

words = jieba.cut(content, cut_all=False)

# print("Output 精確模式 Full Mode：")
for word in words:
    print (word)
