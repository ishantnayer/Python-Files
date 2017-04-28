#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:37:49 2017

@author: IshantNayer
"""

#Question 2
import nltk

#Defining feature functions
def gender_features1(word):
 return {'firstletter': word[0]}

def gender_features2(word): 
  return {'lastletter': word[-1]}
 

def gender_features3(word):
  features = {}
  features['firstletter'] =  word[0].lower()
  features['lastletter']  =  word[-1].lower()
  return features
	  	
#Extracting names
from nltk.corpus import names
ln = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])
import random
random.shuffle(ln)

type(ln)
len(ln)

#Train and Test
tn = ln[1000:]
dn = ln[500:1000]
testn = ln[:500]

#Capture your results, first initialize it
results = []

#Extracting features by First letter
ts   = [(gender_features1(n), g) for (n,g) in tn]
ds = [(gender_features1(n), g) for (n,g) in dn]
tests    = [(gender_features1(n), g) for (n,g) in testn]

classifier = nltk.NaiveBayesClassifier.train(ts)
accuracy   = nltk.classify.accuracy(classifier, ds)

results.append(accuracy)

#Extracting features by Last letter
ts   = [(gender_features2(n), g) for (n,g) in tn]
ds = [(gender_features2(n), g) for (n,g) in dn]
tests    = [(gender_features2(n), g) for (n,g) in testn]

classifier = nltk.NaiveBayesClassifier.train(ts)
accuracy   = nltk.classify.accuracy(classifier, ds)

results.append(accuracy)

#Extracting features by First and Last Letter
ts   = [(gender_features3(n), g) for (n,g) in tn]
ds = [(gender_features3(n), g) for (n,g) in dn]
tests    = [(gender_features3(n), g) for (n,g) in testn]

classifier = nltk.NaiveBayesClassifier.train(ts)
accuracy   = nltk.classify.accuracy(classifier, ds)

results.append(accuracy)

#[0.652, 0.736, 0.756]
# 3rd option performed the best where Extracting features was done by First and Last Letter

#Testing 3rd option accuracy on final test data
accuracy   = nltk.classify.accuracy(classifier, tests)

#Accuracy in test set is 0.78

#Question 3
from nltk.corpus import senseval
instances= senseval.instances('hard.pos')
size= int(len(instances) * 0.1)
ts,tests= instances[size:],instances[:size]

for ins in ts[:10]:
    pos = ins.position
    word = ' '.join(w for (w,t) in ins.context[pos:pos+1])
    left = ' '.join(w for (w,t) in ins.context[pos-2:pos])
    right = ' '.join(w for (w,t) in ins.context[pos+1:pos+3])
    sense = ' '.join(ins.senses)
    print ('%20s |%10s | %-15s -> %s' % (left, word, right, sense))
    
def feature(instance):
    #Empty dictionary
    f= dict() 
    pos= instance.position
    if pos:
        f['wp']= instance.context[pos-1][0]
        f['tp']= instance.context[pos-1][1]
    else:
        f['wp']= (pos,'BOS')
        f['tp']= (pos,'BOS')
        f['wf']= instance.context[pos+1][0]
        f['tf']= instance.context[pos+1][1]
    return f

#Feature set
fset =[(feature(w),w.senses[0]) for w in instances if len(w.senses)==1]

random.shuffle(fset)  

#Building the classifier and predicting
trainclass= fset[1000:] 
devclass= fset[:500]
testclass=fset[500:1000]
buildclass = nltk.NaiveBayesClassifier.train(trainclass)

#Dev Test
devacc= nltk.classify.accuracy(buildclass,devclass) #0.77

#Test accuracy
testacc= nltk.classify.accuracy(buildclass,testclass) #0.794
    
#Question 4

#Create movie review documents
import string
from nltk.corpus import movie_reviews as rev
from nltk.corpus import stopwords
stop = stopwords.words('english')
documents = [([w for w in rev.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in rev.fileids()]
random.shuffle(documents)

#FreqDist of all words
Total_words = nltk.FreqDist(w.lower() for w in rev.words())
wf = list(Total_words)[:2000]

#Classification by feature extraction
def document_features(document):
    document_words = set(document)
    features = {}
    for word in wf:
        features['contains({})'.format(word)] = (word in document_words)
    return features
 	
#Train and Test
fs = [(document_features(d), c) for (d,c) in documents]
ts, tests = fs[100:], fs[:100]
classifier = nltk.NaiveBayesClassifier.train(ts)
nltk.classify.accuracy(classifier, tests) #0.77

# 30 Best features
classifier.show_most_informative_features(30)
#Initially I got ":" as most important feature. After removing stop words, I got better results.
#Reviews containing words like unimaginative, welles are 8.3 times more likely to be negative than positive which is expected.
#No surprises!

#Question 5

#We will use 2 feature extractors to show the difference in the performance of a decision tree, 
#1. Naive Bayes 2. Maximum Entropy

#Feature extractor by Last letter
def gender_features2(word): 
  return {'lastletter': word[-1]}
 
#Feature extractor by First & Last letter
def gender_features3(word):
  features = {}
  features['firstletter'] =  word[0].lower()
  features['lastletter']  =  word[-1].lower()
  return features
 	
#Extracting names
from nltk.corpus import names
ln = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])
import random
random.shuffle(ln)

type(ln) #Class: List
len(ln) #7944

#Train and Test
tn = ln[1000:]
testn = ln[:1000]
len(tn) #6944
len(testn) #1000

results1 = [] 
results2 = [] 

#Extracting features by Last letter
ts = [(gender_features2(n), g) for (n,g) in tn]
tests = [(gender_features2(n), g) for (n,g) in testn]

#Naive Bayes
cnv = nltk.NaiveBayesClassifier.train(ts)
anv = nltk.classify.accuracy(cnv, tests)

results1.append(anv)

#Decision Tree
cdt = nltk.DecisionTreeClassifier.train(ts)
adt = nltk.classify.accuracy(cdt, tests)

results1.append(adt)

#Maximum entropy
cme = nltk.MaxentClassifier.train(ts)
ame = nltk.classify.accuracy(cme, tests)

results1.append(ame)

print ('Accuracy Naive Bayes: {0:.2f}%'.format(anv))
print ('Accuracy Decision Tree: {0:.2f}%'.format(adt))
print ('Accuracy Maximum Entropy: {0:.2f}%'.format(ame))

#Extracting features by First and Last Letter
ts = [(gender_features3(n), g) for (n,g) in tn]
tests = [(gender_features3(n), g) for (n,g) in testn]

#Naive Bayes
cnv = nltk.NaiveBayesClassifier.train(ts)
anv = nltk.classify.accuracy(cnv, tests)

results2.append(anv)

#Decision Tree
cdt = nltk.DecisionTreeClassifier.train(ts)
adt = nltk.classify.accuracy(cdt, tests)

results2.append(adt)

#Maximum Entropy
cme = nltk.MaxentClassifier.train(ts)
ame   = nltk.classify.accuracy(cme, tests)

results2.append(ame)

#Results of all classifiers
results1 #[0.753, 0.753, 0.753] #Same for all 3

#Results of all classifiers for First & Last letters
results2 #[0.765, 0.774, 0.762]

#The accuracy of Decision Tree classifier is the best for First & Last letter classifier
#As expected, First & Last letter feature generator is better than Last letter feature generator

#Question 6
from itertools import chain
from nltk.corpus import wordnet
synonym_strong = wordnet.synsets('strong')
synonym_powerful = wordnet.synsets('powerful')
set(chain.from_iterable([word.lemma_names() for word in synonym_strong]))
set(chain.from_iterable([word.lemma_names() for word in synonym_powerful]))


