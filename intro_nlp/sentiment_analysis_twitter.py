#! /usr/bin/python
# src: https://www.pythonforengineers.com/practice-session-sentiment-analysis-with-twitter/
from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


# check the data structure
# print(twitter_samples.fileids())
# strings = twitter_samples.strings("negative_tweets.json")
# for string in strings[:5]:
#     print(string)

neg_tweets = []
# loop over all the tweets in the negative_tweets
for tweet in twitter_samples.strings("negative_tweets.json"):
    # clean the data out of emotes
    tweet = tweet.replace(":", "").replace(")", "").replace("(", "")
    # get all words in that file
    words = word_tokenize(tweet)
    neg_tweets.append((create_word_features(words), "negative"))
print("Number of negative tweets:", len(neg_tweets))

pos_tweets = []
# loop over all the tweets in the negative_tweets
for tweet in twitter_samples.strings("positive_tweets.json"):
    # clean the data out of emotes
    tweet = tweet.replace(":", "").replace(")", "").replace("(", "")
    # get all words in that file
    words = word_tokenize(tweet)
    pos_tweets.append((create_word_features(words), "positive"))
print("Number of positive tweets:", len(pos_tweets))

# model data split
train_set = neg_tweets[:4000] + pos_tweets[:4000]
test_set = neg_tweets[4000:] + pos_tweets[4000:]
print(len(train_set), "training samples,", len(test_set), "test samples.")

# model training
classifier = NaiveBayesClassifier.train(train_set)

# model accuracy
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print("Model's accuracy: {}%".format(round(accuracy * 100)))
