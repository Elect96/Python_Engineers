# src: https://www.pythonforengineers.com/analysing-the-enron-email-corpus/
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# read the file
with open("ken_lay_emails.txt", "r") as f:
    data = f.read()

# tokenize the file and remove all stop words
words = word_tokenize(data)
useful_words = [word for word in words if word not in stopwords.words("English")]

# frequency of words
frequency = nltk.FreqDist(useful_words)
print(frequency.most_common(100))
