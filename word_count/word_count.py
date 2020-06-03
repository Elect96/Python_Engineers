#! /usr/bin/python
# src: https://www.pythonforengineers.com/create-a-word-counter-in-python/
import sys


def count_words(text):
    words = text.split(" ")
    return len(words)


def count_lines(text):
    lines = text.split("\n")
    for l in lines:
        if not l:
            lines.remove(l)
    return len(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        exit(1)
    # sys.argv[0] - python file; sys.argv[1] - data file
    filename = sys.argv[1]
    f = open(filename, "r")
    data = f.read()
    f.close()

    num_words = count_words(data)
    num_lines = count_lines(data)

    print("The number of words: ", num_words)
    print("The number of lines: ", num_lines)