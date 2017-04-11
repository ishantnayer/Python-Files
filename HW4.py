#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:54:45 2017

@author: IshantNayer
"""

# Q13,15,19,20,21,22,23

#Q13
p, q = 5, 6
word_vowels = [[set() for i in range(p)] for j in range(q)]
example = ['Hello', 'What', 'are', 'you', 'upto', 'today']

for each in word_vowels:
	for word in example:
		v = 0
		l = len(word)
		for letter in word: 
			if letter in "aeiou":
				v += 1
		word_vowels[l][v] = word #Word is added to the matrix according to the length and number of vowels each word contains
print(word_vowels)

# Output: [[set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), set(), set(), set()], [set(), set(), 'you', set(), set()],
#[set(), 'What', 'upto', set(), set()], [set(), set(), 'today', set(), set()]]

#Q15
from nltk import *
my_string = 'sea shore sea shells something something something'
new_string = my_string.split( )
total_words = len(new_string)
fd = FreqDist(new_string)
final = sorted(fd.most_common(total_words))
for f in final:
		print(f)

# ('sea', 2)
# ('shells', 1)
# ('shore', 1)
# ('something', 3)

#Q19
from nltk.corpus import wordnet as wn
whales = [wn.synset(s) for s in
          "minke_whale.n.01, orca.n.01, novel.n.01, tortoise.n.01".split(', ')]
print (whales)

#[Synset('lesser_rorqual.n.01'), Synset('killer_whale.n.01'), Synset('novel.n.01'), Synset('tortoise.n.01')]

def semantic_sort(sslist,ss):
    """return a list of synsets, sorted by similarity to another synset"""
    sim = [(ss.shortest_path_distance(s), s) for s in sslist]
    return [s for (sm, s) in sorted(sim)]

print (semantic_sort(whales, wn.synset('right_whale.n.01')))

#[Synset('lesser_rorqual.n.01'), Synset('killer_whale.n.01'), Synset('tortoise.n.01'), Synset('novel.n.01')]

def semantic_sort1(sslist,ss):
    """return a list of synsets, sorted by similarity to another synset"""
    return sorted(sslist, key=lambda x: ss.shortest_path_distance(x))     
    
print (semantic_sort1(whales, wn.synset('right_whale.n.01')))

#[Synset('lesser_rorqual.n.01'), Synset('killer_whale.n.01'), Synset('tortoise.n.01'), Synset('novel.n.01')]

#Q20
words = ['a', 'b', 'c', 'a', 'b', 'b', 'c', 'd', 'b']

fd = FreqDist(words)
length = len(set(fd))
answer = list(fd.most_common(length))
answer = [i[0] for i in answer]
print(answer)

#['b', 'a', 'c', 'd']

#Q21
from nltk.corpus import genesis

print(set(genesis.words()).difference(['writing', 'another', 'random', 'sentence']))

#Yes, I am able to do that.

#Q22
from operator import itemgetter

words = ['this', 'is', 'my', 'list', 'of', 'words']

sorted(words, key=itemgetter(1))
# ['of', 'this', 'list', 'words', 'is', 'my']

sorted(words, key=itemgetter(-1))
# ['of', 'this', 'is', 'words', 'list', 'my']

#operator.itemgetter(n) constructs a callable that assumes iterable object (list, tuple, set) as input an fetches n-th element out of it.

#Q23
ugly = ['omg', 'you', 'are', 'so', 'ugly', 'sof', 'sofia']

def lookup(trie, key):
	return trie[key]

print(lookup(ugly, 1))

#extend the function

def ext(trie, hint):
    p = [s for s in trie if hint in s]
    if len(p) == 1:
        return p
    else:
        return "Not uniquely determined"
    
print(ext(ugly, 'sof'))














