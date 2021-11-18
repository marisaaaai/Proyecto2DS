'''

        Proyecto 2
        Models

Creado por:

*   María Isabel Montoya Valladares 19169
*   Luis Pedro García Salazar 19344
*   María José Morales Reichenbach 19145
*   Juan Fernando de Leon Quezada  17822

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Import Dataset
cleanData = pd.read_csv("train.csv")

# Split train and Test
X = cleanData
train, test = train_test_split(X, test_size=0.3,train_size=0.7)

X_train = train['new text']
y_train = train['target']
X_test = test['new text']

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

nb = MultinomialNB()
nb.fit(X_train, y_train)

model_VectorizeMultinomialNB = Pipeline([
    ('bow', CountVectorizer()),  # strings to token integ
    ('classifier', MultinomialNB()),  # train on TF-IDF vectors w/ Naive Bayes classifier
])

X_train = train['new text']
y_train = train['target']
X_test = test['new text']
model_VectorizeMultinomialNB.fit(X_train, y_train)

def predictVectorizeMultinomialNB(tweet):
    '''Predict with Vectorize Multinomial NB'''

    return model_VectorizeMultinomialNB.predict(tweet)

