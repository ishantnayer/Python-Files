#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 14:12:41 2017

@author: IshantNayer
"""

#Q13
import nltk
from nltk.corpus import wordnet as wn

all_noun = wn.all_synsets('n')
print(all_noun)
print(wn.all_synsets('n'))
all_num = len(set(all_noun))
noun_have_hypon = [w for w in wn.all_synsets('n') if len(w.hyponyms()) >= 1]
noun_have_num = len(noun_have_hypon)
print('There are %d nouns, and %d nouns w/o hyponyms, the percentage is %f' %
  (all_num, noun_have_num, (all_num-noun_have_num)/all_num*100))

#There are 82115 nouns, and 16693 nouns without hyponyms, the percentage is 79.671193

#Q14
def supergloss(s):
    n = 0
    synset = (s.name, s.definition)
    hypernyms = s.hypernyms()
    hyponyms = s.hyponyms()
    if hypernyms != []:
        while n < len(hypernyms):
            for hypernym in s.hypernyms():
                hypernyms[n] = (hypernym.name, hypernym.definition)
                n = n + 1
    else:
        hypernyms = 'none'
    n = 0
    if hyponyms != []:
        while n < len(hyponyms):
            for hyponym in hyponyms:
                hyponyms[n] = (hyponym.name, hyponym.definition)
                n = n + 1
    else:
        hyponyms = 'none'
    total = 'ROOT WORD:', synset, 'HYPERNYMS:', hypernyms, 'HYPONYMS:', hyponyms
    return total

#Q16
def ld(corpus):
    for genre in corpus.categories():
        ld = len(set(corpus.words(categories=genre)))/len(corpus.words(categories=genre))
        print (genre + ':', ld)
    return 0

#adventure: 0.1279743878169075
#belles_lettres: 0.10642071451679992
#editorial: 0.16054152327770924
#fiction: 0.1358194136199042
#government: 0.11667641228232811
#hobbies: 0.14493897625842492
#humor: 0.23125144042406084
#learned: 0.09268890745953554
#lore: 0.13148804612915801
#mystery: 0.12212912592488936
#news: 0.14314696580941583
#religion: 0.1617553745018909
#reviews: 0.21192020440251572
#romance: 0.12070492131044529
#science_fiction: 0.22342778161713892

#Learned has the lowest diversity. No, we would not have expected this.

#Q17
def cw(text, language):
    fdist = nltk.FreqDist([w.lower() for w in text])
    words = []
    for key in fdist.keys():
        if key not in nltk.corpus.stopwords.words(language):
            words.append(key)
    return words[:50]

#Q18
def top_bigrams(text, language):
	fdist = nltk.probability.FreqDist(nltk.bigrams(text))
	stopwords = nltk.corpus.stopwords.words(language)
	top_list = [(x,y) for x,y in fdist.keys() if x.isalpha() and y.isalpha() and x not in stopwords and y not in stopwords]
	return top_list[:50]

#Q20
def word_freq(word, section):
	freq = nltk.probability.FreqDist(nltk.corpus.brown.words(categories = section))
	word_frequency = freq[word]
	return word_frequency

#Q22
def hedge(text):
    n = 3
    like = list(text)
    while n <= len(like):
        like.insert(n, 'like')
        n = n + 4
    for w in like:
        print (w)



















