#! /usr/bin/python
# src: https://www.pythonforengineers.com/build-a-sentiment-analysis-app-with-movie-reviews/
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet


# this is how the Naive Bayes classifier expects the input
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return  my_dict


neg_reviews = []
# loop over all the files in the neg folder
for file_id in movie_reviews.fileids("neg"):
    # get all the words in that file
    words = movie_reviews.words(file_id)
    neg_reviews.append((create_word_features(words), "negative"))
print("Number of negative reviews:", len(neg_reviews))

pos_reviews = []
# loop over all the files in the pos folder
for file_id in movie_reviews.fileids("pos"):
    # get all the words in that file
    words = movie_reviews.words(file_id)
    pos_reviews.append((create_word_features(words), "positive"))
print("Number of positive reviews:", len(pos_reviews))

train_set = neg_reviews[:750] + pos_reviews[:750]
test_set = neg_reviews[750:] + pos_reviews[750:]
print(len(train_set), "training samples,", len(test_set), "test samples.")

classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print("Model's accuracy: ", accuracy * 100)

# testing the model with some Imdb reviews
review_santa = '''It would be impossible to sum up all the stuff that sucks about this film, so I'll break it down into 
what I remember most strongly: a man in an ingeniously fake-looking polar bear costume (funnier than the "bear" 
from Hercules in New York); an extra with the most unnatural laugh you're ever likely to hear; 
an ex-dope addict martian with tics; 
kid actors who make sure every syllable of their lines are slowly and caaarreee-fulll-yyy prrooo-noun-ceeed; 
a newspaper headline stating that Santa's been "kidnaped", and a giant robot. Yes, you read that right. A giant robot.
The worst acting job in here must be when Mother Claus and her elves have been "frozen" by the "Martians'" weapons. 
Could they be *more* trembling? I know this was the sixties and everyone was doped up, but still.'''
review_spirit = '''Spirited Away' is the first Miyazaki I have seen, but from this stupendous film I can tell he is a master storyteller. 
A hallmark of a good storyteller is making the audience empathise or pull them into the shoes of the central character. 
Miyazaki does this brilliantly in 'Spirited Away'. During the first fifteen minutes we have no idea what is going on. 
Neither does the main character Chihiro. We discover the world as Chihiro does and it's truly amazing to watch. 
But Miyazaki doesn't seem to treat this world as something amazing. The world is filmed just like our workaday world would. 
The inhabitants of the world go about their daily business as usual as full with apathy as us normal folks. 
Places and buildings are not greeted by towering establishing shots and majestic music. The fact that this place is amazing doesn't seem to concern Miyazaki.
What do however, are the characters. Miyazaki lingers upon the characters as if they were actors. 
He infixes his animated actors with such subtleties that I have never seen, even from animation giants Pixar. 
Twenty minutes into this film and I completely forgot these were animated characters; 
I started to care for them like they were living and breathing. 
Miyazaki treats the modest achievements of Chihiro with unashamed bombast. 
The uplifting scene where she cleanses the River God is accompanied by stirring music and is 
as exciting as watching gladiatorial combatants fight. 
Of course, by giving the audience developed characters to care about, the action and conflicts will always be more 
exciting, terrifying and uplifting than normal, generic action scenes.'''

words = word_tokenize(review_santa)
words = create_word_features(words)
print("Santa's review is marked as:", classifier.classify(words))

words = word_tokenize(review_spirit)
words = create_word_features(words)
print("Spirited's review is marked as:", classifier.classify(words))
