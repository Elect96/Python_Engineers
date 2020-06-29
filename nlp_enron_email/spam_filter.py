# src: https://www.pythonforengineers.com/build-a-spam-filter/
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import random
from sklearn.externals import joblib


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


root_dir = "C:\\Users\\polgl\\Downloads\\enron_spam\\enron1"
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
                ham_list.append((create_word_features(words), "ham"))
    # check if spam folder
    if os.path.split(directories)[1] == "spam":
        for filename in files:
            with open(os.path.join(directories, filename), encoding="latin-1") as f:
                data = f.read()
                # tokenize the data
                words = word_tokenize(data)
                # prepare the data to be used for Naive Bayes
                spam_list.append((create_word_features(words), "spam"))

# combine both lists
combined_list = ham_list + spam_list
random.shuffle(combined_list)

# allocate 70% of data for training and 30% for testing
split_point = int(len(combined_list) * .7)
train_set = combined_list[:split_point]
test_set = combined_list[split_point:]
print(len(train_set), "training samples,", len(test_set), "testing samples.")

# train the model
classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print("Accuracy is:", accuracy * 100)

# save the model to a file
joblib.dump(classifier, "enron_model", compress=9)