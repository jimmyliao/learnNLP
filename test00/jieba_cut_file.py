#encoding=utf-8
import jieba
import sys
import jieba.posseg as pseg

# Dict file from https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big

#jieba.set_dictionary('./dict.txt.big')

# content = open('input.txt', 'rb').read()

# print "Input：", content

##### Trial #1 斷詞
# words = jieba.cut(content, cut_all=False)
# processed_words = list(words)
#
# for word in processed_words:
# 	sys.stdout.write(word.encode('utf-8') + ',')


##### Trial #2 磁性
# words = pseg.cut(content)
#
# print "Output 精確模式 Full Mode："
# for word in words:
#     print word.word, word.flag
#     print word

with open('./input.txt') as f:
    tmp_line = f.read()

    tmp_line_decode = tmp_line.decode('utf-8')
    jieba_cut = jieba.cut(tmp_line_decode)
    # ans = '/'.join(jieba_cut)
    ## To integrate with NLTK, need to use space
    ans = ' '.join(jieba_cut)
    ans = ans.encode('utf-8')
    with open('./result.txt', 'w') as f2:
        f2.write(ans)
