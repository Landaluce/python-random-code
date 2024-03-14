#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
import random
# Pig Cypher original codes
# ab cd ef      st
# gh ij kl  uv      wx
# mn op qr      yz
#
# ul uc ur
# ml mc mr
# dl dc dr
# u  l  r
# d

length_of_code = 5
letters = list(string.ascii_letters)
digits = list(string.digits)
punctuation = list(string.punctuation)
alphabet = letters + digits + punctuation + [" ", "\n"]
codes = ['6DD38', '/o^Jn', 'RX:wA', 'X(|El', 'H6"O+', '57>\n8', '(:,po', '/m~P\\', 'n,&[Z', '2@L@W', '\\$j,m',
         'gRk>s', 'q1MS[', 'T%SMb', 'hgs3r', 'x}5:5', "/1b'#", 'KBzI=', 'av_~H', 'N;BoL', '#Qz3R', '&*O^o', 'w|hSA',
         '%^b20', 'z5Jf?', '1I-3?', '/{{g>', '*=J"!', '|?oUC', '.hUhT', 'E(+JP', '*K`"`', 'Pg2jW', '%qD?(', 'U.deX',
         'A$g#M', '[5Ann', 'baB1*', 'qu>V)', '3=AsS', '@s(}=', 'gVc8&', ':F:-F', 'QVnlF', '82t}p', ']q.,H', 'j$C9y',
         'r)2;=', 'QdWow', 'P(]0`', 'qfiBu', '<${p<', '/_n^^', 'C#S\\c', 'tU(Jm', 'hkL+V', 'K@)(+', '3PQyK',
         'NCqOY', 'Q0({&', 'cVfmZ', '0@<;`', 'xSA6.', 's-@e@', '8SE1)', 'NEf!T', '{\\gYO', 'YstW{', '[deom',
         'Txn-V', 'c8@KT', '2E<8[', 'IoTKQ', 't<=[o', '.=,j/', '@+Rv&', '#G%RF', 'ZV2:^', ']AIP"', '?"\n^O',
         'j;[iL', '(FE(e', '~yu!l', '!VK|=', '2/XPg', 'lUF*D', '9+%U1', 'd.AF[', 'b?94:', 'k1TwR', 'V48+4', 'ddHc+',
         'WLUb?', '-WZ$+', 'H<<Ds', 'IqW![', '){LcK']


def generate_codes():
    codes = []
    while len(codes) <= len(alphabet):
        # Pig Cyper original codes
        # length = 3 :1 letter + 2 digits
        # letter_index = random_number(count=1, max_value=len(letters))
        # letter = letters[letter_index[0]]
        # number = random_number(count=1, min_value=10, max_value=99)
        # code = letter + str(number[0])

        # my codes
        code = ""
        while len(code) < length_of_code:
            index = random_number(count=1, max_value=len(alphabet))
            letter = alphabet[index[0]]
            if " " not in letter:
                code += letter
        print(code)

    print(len(codes), codes)


def get_shifted_codes(key: int = 0, generate: bool = False):
    if generate:
        new_codes = []
        while len(new_codes) < len(alphabet):
            code = ""
            while len(code) < length_of_code:
                index = random_number(count=1, max_value=len(alphabet))
                letter = alphabet[index[0]]
                if " " not in letter:
                    code += letter
            new_codes.append(code)
        return new_codes[key:] + new_codes[:key]
    return codes[key:] + codes[:key]


def random_number(start=0, count=1, min_value=0, max_value=1):
    random_lst = []
    for i in range(start, count):
        y = random.randrange(min_value, max_value)
        random_lst.append(y)
    return random_lst


def cypher(message: str, codes: list):
    secret = ""
    for i in message:
        try:
            index = alphabet.index(i)
            secret += codes[index]
        except ValueError:
            secret += i
    return secret


def de_cypher(secret: str, codes: list):
    message = ""
    for i in range(0, len(secret), length_of_code):
        code = secret[i:i + length_of_code]
        index = codes.index(code)
        message += alphabet[index]
    return message


def main():
    # generate_codes()
    key = 8
    my_codes = get_shifted_codes(key=key)
    message = "Secret Message!\nsecond line."
    print(message)

    secret = cypher(message, my_codes)
    print(secret)

    print(de_cypher(secret, my_codes))


if __name__ == "__main__":
    main()
