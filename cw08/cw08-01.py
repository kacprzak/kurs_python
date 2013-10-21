#!/usr/bin/env python3
# cw08-01

import sys

def silnia(n):
    """Oblicza silnię z n"""
    if n < 0:
        raise ValueError
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
    

if len(sys.argv) < 2:
    print('Nie podano argumentu!')
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print('Argument nie jest liczbą całkowitą!')
    sys.exit()

try:
    print('{}! = {}'.format(n, silnia(n)))
except ValueError:
    print('Argument nie może być mniejszy od zera!')
