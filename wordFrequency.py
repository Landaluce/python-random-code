#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
from collections import Counter


def get_word_frequency(filename):
    with open(filename, "r") as file:
        content = file.read().replace('\n', ' ')

    content = content.translate(str.maketrans('', '', string.punctuation)).lower()
    word_list = content.split()

    # Use Counter for counting word occurrences
    word_counter = Counter(word_list)

    # Convert Counter to a list of tuples (count, word)
    result = [(count, word) for word, count in word_counter.items() if word]

    # Sort the result by count in descending order
    result = sorted(result, key=lambda x: x[0], reverse=True)

    return result


def main():
    frequency = get_word_frequency("sample_text.txt")
    print(frequency)


if __name__ == "__main__":
    main()
