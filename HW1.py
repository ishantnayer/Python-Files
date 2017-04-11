#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:27:25 2017

@author: IshantNayer
"""

#Q18
sent_total = sent1+sent2+sent3+sent4+sent5+sent6+sent7+sent8
sent_vocab = sorted(set(sent_total))
sent_vocab

#Q19
len(sorted(set(w.lower() for w in text1)))  ## Case1; 17231 
len(sorted(w.lower() for w in set(text1)))  ## Case2; 19317

# Explanation for 19
# For Case1, every word type is first converted to a lower case for text1 and then applied with the set() function. Therefore words like 'there' and 'There' are sonsidered the same.
# For Case2, The words are first applied with set() and then converted to lower case. This still counts 'There' and 'there' as 2 different words.

#Q20
example="Hello World"

example.isupper()  ## checks if all elements are in upper case; returns false
example.islower()  ## checks if all elements are in lower case; returns false
not example.islower() ## First checks if all elements are in lower case, then does a negation; returns True

#Q21
text2[-2:] ## ['THE', 'END']

#Q22
flw = [w.lower() for w in text5 if len(w) == 4 and w.isalpha()]
freq = FreqDist(flw)
freq #In decreasing order
#FreqDist({'part': 1022, 'join': 1021, 'that': 284, 'what': 201, 'here': 185, 'have': 171, 'like': 160, 'with': 154, 'chat': 146, 'your': 142, ...})
      
#Q24
# a. Ending in ize              
[w for w in set(text6) if w.endswith('ize')] #Blank

# b. Containing the letter z
sorted(w for w in set(text6) if 'z' in w.lower()) #['AMAZING', 'Fetchez', 'ZOOT', 'Zoot', 'amazes', 'frozen', 'zhiv', 'zone', 'zoo', 'zoop', 'zoosh']

# c. Containing the sequence of letters pt
sorted([w for w in set(text6) if 'pt' in w.lower()]) #[‘Chapter', 'Thpppppt', 'Thppppt', 'Thpppt', 'Thppt', 'aptly', 'empty', 'excepting', 'ptoo', 'temptation', 'temptress']

# d. Having all lowercase letters except for an initial capital (i.e., titlecase)
sorted([w for w in set(text6) if w.istitle()]) #All title case words

#Q25
sent=['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

# a. Print all words beginning with sh
[w for w in sent if w.startswith("sh")] #['she', 'shells', 'shore']

# b. Print all words longer than four characters
[w for w in sent if len(w)>4] #['sells', 'shells', 'shore']

#Q26
sum(len(w) for w in text1) # adds the length of each word in text 1; 999044

avg= sum(len(w) for w in text1)/len(text1)
avg  # 3.830411128023649

#Q27
def vocab_size(text):
    return len(sorted(set(text)))
    
vocab_size(text6) # 2166
 
#Q28 
def percent(word, text):
    freq=(100*len([w for w in text if w==word]))/len(text)
    return freq
    
percent('how',text4)
# 0.018526778056060657
