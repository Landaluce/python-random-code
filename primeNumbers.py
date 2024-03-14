#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import isqrt
from typing import List


def primes_under_n(n: int):
    return [x for x in range(2, n + 1) if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))]


def get_n_primes(n: int):
    return [num for num in range(2, n * (n + 1)) if is_prime(num)][:n]


def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def print_list(lst: List):
    c = 1
    for n in lst:
        if n > c * 100:
            c += 1
            print("\n" + str(n), end=", ")
        else:
            print(n, end=", ")


def main():
    n = 200
    primes = get_n_primes(n)
    # print(primes[n-1])
    print_list(primes)


if __name__ == "__main__":
    main()
