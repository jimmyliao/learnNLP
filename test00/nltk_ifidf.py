corpus_root = './'

allText = ''

#allText = PlaintextCorpusReader(corpus_root, ['comment4.txt', 'comment5.txt'])
#allText = PlaintextCorpusReader(corpus_root, ['result.txt'])
allText = PlaintextCorpusReader('result.txt')

print type(allText)

sinica_text = nltk.Text(allText.words())

mytexts = TextCollection(allText)

print len(mytexts._texts)

print len(mytexts)

the_set = set(sinica_text)
print len(the_set)
for tmp in the_set:
    print tmp, "tf", mytexts.tf(tmp, allText.raw(['result.txt'])), "idf", mytexts.idf(tmp), mytexts.tf_idf(tmp, allText.raw(['result.txt']))
