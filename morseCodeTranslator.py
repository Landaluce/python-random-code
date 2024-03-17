#!/usr/bin/env python
# -*- coding: utf-8 -*-

table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ",--,",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "=": "-...-",
    " ": "/",
}


def text_to_morse(text):
    mc = ""
    for letter in text:
        mc += table[letter] + " "
    return mc


def morse_to_text(morse):
    text = ""
    morse = morse.split(" ")
    for letter in morse:
        for key, value in table.items():
            if value == letter:
                text += key
    return text


def main():
    msg = "HELLO WORLD"
    morse = text_to_morse(msg)
    print(morse)
    text = morse_to_text(morse)
    print(text)


if __name__ == "__main__":
    main()
