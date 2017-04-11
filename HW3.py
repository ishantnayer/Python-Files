#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 01:43:34 2017

@author: IshantNayer
"""

#Questions 18, 19, 21, 23, 24, 27, 31, 32

#Q18
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
tokens = word_tokenize(raw)
wh_words = [w for w in tokens if w.startswith('wh')]
wh_words.sort()
print(wh_words)

#Q19
f = open("in.txt").readlines()
f = [line.strip() for line in f]
result = [line.split(' ') for line in f]
for item in result:
	item[1] = int(item[1]) 
print(result)

#Q21
from nltk.corpus import words
from bs4 import BeautifulSoup
def unknown(url):
	html = request.urlopen(url).read().decode('utf8')
	raw = BeautifulSoup(html).get_text()
	corpus_words = set(words.words())
	lower_case_words = re.findall(r'\b[a-z]+', raw)
	unknowns = [word for word in lower_case_words if word not in corpus_words]
	print(unknowns)

unknown('http://www.nltk.org/book/ch01.html')

#Q23
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
matches = re.findall(r'\b(do)(n\'t)', raw)
print(matches)
# the regex it gives won't work because it doesn't escape the single 
#quote. also because it's looking for either n't or one or more word 
#characters. So it'll return everyhing

#Q24
raw = raw.lower()
def convert_to_hacker(text):
	new_text = []
	pattern = re.compile(r'ate')
	text = pattern.sub('8', text) 
	pattern = re.compile(r'[eiols]|\.')
	for w in text:
		if re.search(pattern, w):
			if w == 'e':
				w = '3'
			elif w == 'i':
				w = '1'
			elif w == 'o':
				w = '0'
			elif w == 's':
				w = '5'
			elif w == 'l':
				w = '|'
			elif w == '.':
				w = '5w33t!'
		new_text.extend(w)
	new_text = ''.join(new_text)
	pattern = re.compile(r'\b5')
	new_text = pattern.sub('$', new_text)
	return new_text

text = convert_to_hacker(raw)
print(text)

#Q27
from random import choice

str = ''.join(list((choice("aehh ") for x in range(500))))
str = str.split(' ')
str = ''.join(str)
print(str)

#Q31
saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']

lengths = []
for w in saying:
	lengths.append(len(w))
    
print(lengths)

lengths = [len(w) for w in saying]
print(lengths)

#Q32
silly = 'newly formed bland ideas are inexpressible in an infuriating way'

bland = silly.split(' ')

silly_word = ''

for word in bland:
	silly_word += word[1]
print(silly_word)

new_bland = ' '.join(bland)
print(new_bland)
print(bland)

bland = sorted(bland)
for w in bland:
	print(w)