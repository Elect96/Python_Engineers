# src: https://www.pythonforengineers.com/build-a-spam-filter/
import os
from nltk.corpus import twitter_samples
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


root_dir = "C:\\Users\\polgl\\Downloads\\enron_spam\\"
ham_list = []
spam_list = []

# loop over the directories
for directories, subdirectories, files in os.walk(root_dir):
    # check if ham folder
    if os.path.split(directories)[1] == "ham":
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                data = f.read()
                # tokenize the data
                words = word_tokenize(data)
                # prepare the data to be used for Naive Bayes
                ham_list.append(create_word_features(words))
    # check if spam folder
    if os.path.split(directories)[1] == "spam":
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                data = f.read()
                # tokenize the data
                words = word_tokenize(data)
                # prepare the data to be used for Naive Bayes
                spam_list.append(create_word_features(words))


print(ham_list[0])
print(spam_list[0])

# TODO: Create the test/train data


