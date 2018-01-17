#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 11:44:15 2017

@author: IshantNayer
"""

from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import ensemble
import numpy as np
import matplotlib.pyplot as plt

train_data = pd.read_csv('PizzaTrain.csv')

print(train_data.head())

train_data.describe()
train_data.dtypes
print(train_data.head())

train_data.shape #(4040, 32)

train_data1 = train_data.select_dtypes(exclude=['object'])
train_data1.dtypes

print(train_data1.describe())

X = train_data1.drop('requester_received_pizza', axis = 1)
Y = train_data1['requester_received_pizza']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
test_size = 0.20, random_state = None)

print(X_train.shape)
print(Y_train.shape)

#Regularized model as learning rate <0.1
final_params = {'n_estimators': 1000, 'max_leaf_nodes': 4, 'max_depth': None, 'random_state': 2,
                   'min_samples_split': 5}

model1 = ensemble.GradientBoostingClassifier(**final_params)
model1.fit(X_train, Y_train)

#Original model
original_params = {'n_estimators': 1000, 'max_leaf_nodes': 4, 'max_depth': None, 'random_state': 2,
                   'min_samples_split': 5, 'learning_rate':1}

model2 = ensemble.GradientBoostingClassifier(**original_params)
model2.fit(X_train, Y_train)

#Scoring
model1.score(X_train, Y_train) #0.95977
model2.score(X_train, Y_train) #0.99876

#Generate class probabilities
probs1 = model1.predict_proba(X_test)
probs2 = model2.predict_proba(X_test)

from sklearn.metrics import roc_auc_score

roc_auc_score(Y_test, probs1[:, 1]) #0.89345
roc_auc_score(Y_test, probs2[:, 1]) #0.85054

# compute test set deviance
test_deviance = np.zeros((final_params['n_estimators'],), dtype=np.float64)
for i, y_pred in enumerate(model1.staged_decision_function(X_test)):
        # clf.loss_ assumes that Y_test[i] in {0, 1}
        test_deviance[i] = model1.loss_(Y_test, y_pred)

#Plot
plt.plot((np.arange(test_deviance.shape[0]) + 1)[::5], test_deviance[::5],
            '-', color='red')

plt.legend(loc='upper left')
plt.xlabel('Boosting Iterations')
plt.ylabel('Test Set Deviance')
plt.show()




