# -*- coding:utf-8 -*-
# Author：jimmyliao
# Date: 2016-06-15
# Reference: http://www.nltk.org/book/ch07.html
# Reference: https://gist.github.com/onyxfish/322906
import nltk, re, pprint
from nltk.corpus import sinica_treebank
from nltk.book import *

with open('gbsc_corpus/file1.txt', 'r') as f:
    sample = f.read()

sentences = nltk.sent_tokenize(sample)
# print ('===== token' + sentences)

tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
print (tokenized_sentences)

# text = nltk.word_tokenize("And now for something completely different")
#
# tagger = nltk.pos_tag(text)
# print ('===== tagger')
# print (tagger)

### Tagger one
# tagged_token = nltk.tag.str2tuple('我/OTHER')
# print (tagged_token)

sent = '我/AT 下午/JJ 要/NN 去/VBD 繳費/IN 信用卡/AT 7-11/NN'

[nltk.tag.str2tuple(t) for t in sent.split()]

tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
print (tagged_sentences)

# chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)
# print (chunked_sentences)


# def extract_entity_names(t):
#     entity_names = []
#
#     if hasattr(t, 'label') and t.label:
#         if t.label() == 'NE':
#             entity_names.append(' '.join([child[0] for child in t]))
#         else:
#             for child in t:
#                 entity_names.extend(extract_entity_names(child))
#
#     return entity_names

# entity_names = []
# for tree in chunked_sentences:
#     # Print results per sentence
#     extract_entity_names(tree)
#     # entity_names.extend(extract_entity_names(tree))
#
# # Print all entity names
# # print (entity_names)
#
# grammar = r"""
#   NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
#   PP: {<IN><NP>}               # Chunk prepositions followed by NP
#   VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
#   CLAUSE: {<NP><VP>}           # Chunk NP, VP
#   """
# cp = nltk.RegexpParser(grammar)

# cp.parse(chunked_sentences)
