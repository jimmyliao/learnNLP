# -*- coding:utf-8 -*-
# Author：jimmyliao
# Date: 2016-06-15
import nltk.tag, nltk.data
from nltk import word_tokenize
from nltk.tag.perceptron import PerceptronTagger

class BackoffTagger:
    def __init__(self):
        self._taggers = [PerceptronTagger()]

model = {'example_one': 'VB', 'example_two': 'NN'}
tagger = nltk.tag.UnigramTagger(model=model, backoff=BackoffTagger())
rlt1 = tagger.tag(['example_one'])
print (rlt1)

tagger = PerceptronTagger(load=False)
tagger.train([[('today','NN'),('is','VBZ'),('good','JJ'),('day','NN')] ])
rlt2 = tagger.tag(['today','is','a','beautiful','day'])
print (rlt2)

tagger = PerceptronTagger(load=False)
tagger.train([[('我','OTHER'),('下午','TIME'),('要','OTHER'),('去','OTHER'),('繳費','OTHER'),('信用卡','NOUN'),('7-11','STORE')] ])
rlt3 = tagger.tag(['我', '下午', '要', '去', '繳費'])
print (rlt3)
