# -*- coding:utf-8 -*-
# Author：jimmyliao
# Date: 2016-06-14
import nltk, re, pprint
from nltk.corpus import sinica_treebank

sent = nltk.corpus.treebank.tagged_sents()[100]
print(nltk.ne_chunk(sent, binary=True))
# for (key, var) in nltk.corpus.treebank.tagged_sents()[:100]:
#     print '%s/%s' % (key, var),
# sent = nltk.corpus.sinica_treebank.tagged_sents()[22]
# print(nltk.ne_chunk(sent))
# for (key, var) in sinica_treebank.tagged_sents()[:100]:
#     print '%s/%s' % (key, var),
