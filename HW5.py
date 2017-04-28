#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 09:34:15 2017

@author: IshantNayer
"""

#Question 15

import nltk
nltk.download()
from nltk.corpus import brown

words = nltk.corpus.brown.words()
tagged = nltk.corpus.brown.tagged_words()
tagged_w= nltk.corpus.brown.tagged_words(tagset='universal')

frequency = nltk.defaultdict(int)

#Identifies words tagged as nouns

for w in [w.lower() for (w,tag) in tagged if tag.startswith('N')]:
    frequency[w] +=1
             
for w in frequency:
    if w+'s' in frequency and frequency[w+'s'] > frequency[w]:
        print ("%s (%d, %d)" % (w, frequency[w+'s'], frequency[w]))
   
#Distinct tags
ditag = nltk.defaultdict(set)

#Tags for each word
for w,tag  in  tagged:
    ditag[w.lower()].add(tag)
maxl = max(len(ditag[w]) for w in ditag)

#Print maxlength words
print  ([(w, t) for w,t  in ditag.items() if len(t) == maxl])

# 20 frequent tags
most_tags = nltk.FreqDist(tag for (word,tag)  in  tagged)
most_tags.most_common(20)

#Tags nouns
bt =nltk.bigrams(t for (w,t)  in  tagged_w)

# fd for all tags followed by noun
tnoun = nltk.FreqDist(x for (x,y)  in  bt if y == 'NOUN')
tnoun.most_common()

#Question 18
cfreq = nltk.ConditionalFreqDist(tagged_w)

#Freq tags
ftgs = cfreq.conditions()
sim= [tag for tag in ftgs if len(cfreq[tag]) == 1]
print(len(sim)/len(ftgs))

#Ambiguous words
am= [tag for tag in ftgs if tag not in sim]
print(len(am))

#Proportion 
token = set(nltk.corpus.brown.words())
ambrown = [w for w in am if w in token]
percent = len(ambrown)/len(token)*100
print(percent)

#Question 21
tagged_w= nltk.corpus.brown.tagged_words(tagset='universal')

#Bigrams
bigram_tag = list(nltk.bigrams(tagged_w))

#Adverbs and preceeded by 4 given words
for b in bigram_tag:
    tlist = [list(t) for t in zip(*b)]
    if tlist[0][1] in ['adore','love','prefer','like'] and tlist[1][1]=='VERB' and tlist[1][0]=='ADV':
        print(tlist[0][0])

#Question 22
tagged_w= nltk.corpus.brown.tagged_words(tagset='universal')
brown_s = nltk.corpus.brown.sents(categories='romance')

other_pat = [(r'.*', 'NN'),(r'.*s$', 'NNS'),(r'.*ing$', 'VBG'),(r'.*ed$', 'VBD'),(r'.*\'s', 'NN$')]
ret = nltk.RegexpTagger(other_pat)
ret.tag(brown_s[10])

#Question 26
import pylab

def performance(cfd, wordlist):

    lt = dict((word, cfd[word].max()) for word in wordlist)

    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))

    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    wf = nltk.FreqDist(brown.words(categories='news')).most_common()
    wbf = [w for (w, _) in wf]
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)

    perfs = [performance(cfd, wbf[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')

    # Sets all of the axes
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

display()


#Question 29
st = brown.tagged_sents(categories='romance')
trained = st[0]
training = brown.sents()[0]
mixed = sorted(training)
tb = list(nltk.bigrams(mixed))
mb = list(nltk.bigrams(training))

def unknown(a,b):
    if list(set(a)-set(b)):
        print("Unknown Contexts")
    else:
        print("Known Contexts")

unknown(tb, mb)

#Question 30

ts = nltk.corpus.brown.tagged_sents(categories='romance')

freq = nltk.FreqDist(nltk.corpus.brown.words())

highfreq =[t for t,w in freq.most_common()]

def low_Freq(w,t):
    if w in highfreq:
        return w
    else:
        return 'UNK'

train_size = int(len(ts) * 0.75)
train_sent = ts[:train_size]
test_sent  = ts[train_size:]
one = nltk.DefaultTagger('NN')
two = nltk.UnigramTagger(train_sent,backoff=one)
three  = nltk.BigramTagger(train_sent,backoff=two)

print(three.evaluate(test_sent))

#Question 31
def display():
        import pylab
        wf = nltk.FreqDist(brown.words(categories='news')).most_common()
        wbf = [w for (w, _) in wf]
        cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
        sizes = 2 ** pylab.arange(15)
        perfs = [performance(cfd, wbf[:size]) for size in sizes]
        pylab.semilogx(sizes, perfs, '-bo')
        pylab.title('Lookup Tagger Performance with Varying Model Size')
        pylab.xlabel('Model Size')
        pylab.ylabel('Performance')
        pylab.show()

display()
