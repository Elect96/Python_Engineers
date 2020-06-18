#! /usr/bin/python
# src: https://www.pythonforengineers.com/build-a-sentiment-analysis-app-with-movie-reviews/
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

