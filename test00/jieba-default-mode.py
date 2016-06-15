#encoding=utf-8
import jieba

sentence = "我要去7-11繳費"
print "Input：", sentence
words = jieba.cut(sentence, cut_all=False)
print "Output 精確模式 Full Mode："
for word in words:
    print word
