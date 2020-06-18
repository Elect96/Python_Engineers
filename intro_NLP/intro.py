#! /usr/bin/python
# src: https://www.pythonforengineers.com/introduction-to-nltk-natural-language-processing-with-python/
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


# sample sentence
sentence = "The Quick brown fox, Jumps over the lazy little dog. Hello World."
# print(sentence.split(" "))

w = word_tokenize(sentence)
# print(nltk.pos_tag(w))

# syn = wordnet.synsets("computer")
# print(syn)
# print(syn[0].name())
# print(syn[0].definition())
#
# print(syn[1].name())
# print(syn[1].definition())
#
# syn = wordnet.synsets("talk")
# print(syn[0].examples())

# antonym of a word
syn = wordnet.synsets("good")
for s in syn:
    for l in s.lemmas():
        if l.antonyms():
            print(l.antonyms())

# similar words
syn = wordnet.synsets("book")
for s in syn:
    print(s.lemmas())

