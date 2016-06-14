# -*- coding:utf-8 -*-
# Author：jimmyliao
# Date: 2016-06-14
import nltk
from nltk.corpus import sinica_treebank

sinica_text = nltk.Text(sinica_treebank.words())
print (sinica_text)
# for (key, var) in sinica_treebank.tagged_words()[:100]:
#     print '%s/%s' % (key, var),
# print sinica_text.concordance(u'我')
# print (sinica_text.concordance('我') ) # python 3

sinica_fd=nltk.FreqDist(sinica_treebank.words())
print (sinica_fd)
# top100=list(sinica_fd.keys())
top100=sinica_fd.keys()

# top100=sinica_fd.items()[0:100]
for (x) in top100:
    print (x)
