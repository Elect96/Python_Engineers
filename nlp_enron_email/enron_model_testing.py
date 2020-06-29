# src: https://www.pythonforengineers.com/build-a-spam-filter/
from sklearn.externals import joblib
from spam_filter import create_word_features
from nltk.tokenize import word_tokenize

print("before test data")
# test data
msg1 = '''Hello th̓ere seُx master :-)
i need c0ck ri͏ght noِw ..͏. don't tell my hǔbbٚy.ٚ. ))
My sc͕rٞeٚe̻nname is Dorry.
My accֺo֔unt is h֯ere: http:nxusxbnd.GirlsBadoo.ru
C u late٘r!'''


msg2 = '''As one of our top customers we are providing 10% OFF the total of your next used book purchase from www.letthestoriesliveon.com. Please use the promotional code, TOPTENOFF at checkout. Limited to 1 use per customer. All books have free shipping within the contiguous 48 United States and there is no minimum purchase.

We have millions of used books in stock that are up to 90% off MRSP and add tens of thousands of new items every day. Don’t forget to check back frequently for new arrivals.'''



msg3 = '''To start off, I have a 6 new videos + transcripts in the members section. In it, we analyse the Enron email dataset, half a million files, spread over 2.5GB. It's about 1.5 hours of  video.

I have also created a Conda environment for running the code (both free and member lessons). This is to ensure everyone is running the same version of libraries, preventing the Works on my machine problems. If you get a second, do you mind trying it here?'''
print("before load the model")
# load the model
model = joblib.load("enron_model")
print("before msg1 pred")
# msg1 prediction
words = word_tokenize(msg1)
features = create_word_features(words)
print("Message 1 is:", model.classify(features))

# msg2 prediction
words = word_tokenize(msg2)
features = create_word_features(words)
print("Message 2 is:", model.classify(features))

# msg3 prediction
words = word_tokenize(msg3)
features = create_word_features(words)
print("Message 3 is:", model.classify(features))

# TODO: it doesn't load, check the create_word_features import first
