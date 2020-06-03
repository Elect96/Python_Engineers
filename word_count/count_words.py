#! /usr/bin/python
# src: https://www.pythonforengineers.com/create-a-word-counter-in-python/
f = open("birds.txt", "r")
data = f.read()
f.close()

words = data.split(" ")

print("The words in the text are:")
print(words)
print("The number of words is ", len(words))
