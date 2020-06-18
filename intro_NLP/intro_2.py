#! /usr/bin/python
# src: https://www.pythonforengineers.com/introduction-to-nltk-natural-language-processing-with-python/
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# stop words
# print(stopwords.words("english")[:16])

paragraph = "The program was open to all women between the ages of 17 and 35, in good health, " \
            "who had graduated from an accredited high school. "
words = word_tokenize(paragraph)
print(words)

useful_words = [word for word in words if word not in stopwords.words("english")]
print(useful_words)

# frequency distribution of the words from move_reviews corpus
all_words = movie_reviews.words()
freq_dist = nltk.FreqDist(all_words)
print(freq_dist.most_common(20))