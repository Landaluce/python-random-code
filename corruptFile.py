#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import os


def corrupt(file="uncorrupted.txt"):
    input_file = os.path.basename(file)
    filename, extension = os.path.splitext(input_file)

    with open(file, 'rb') as f:
        file_content = bytearray(f.read())

    amount = len(file_content)
    variant = 100
    random.seed(len(file_content))
    amount = min(len(file_content), amount)
    victims = random.sample(range(len(file_content)), amount)

    for v in victims:
        file_content[v] = (file_content[v] + variant) % 256

    output_filename = f"{filename}_corrupted{extension}"

    with open(output_filename, 'wb') as output:
        output.write(file_content)


if __name__ == "__main__":
    corrupt()