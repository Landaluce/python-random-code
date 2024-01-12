#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


def reverse_words(input: str):
    words: List[str] = input.split()
    for i in range(0, len(words)):
        words[i] = words[i][::-1]
    print(" ".join(words))


def main():
    reverse_words("Hello World")
    reverse_words("Coding Challenge")

    # Input: "Hello World"
    # Output: "olleH dlroW"

    # Input: "Coding Challenge"
    # Output: "gnidoC egnellehC"


if __name__ == "__main__":
    main()
