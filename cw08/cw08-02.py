#!/usr/bin/env python3
# cw08-02

import sys

def silnia(n):
    """Rekurencyjnie oblicza silnię z n"""
    if n <= 1:
        return 1
    else:
        return n * silnia(n - 1)
    

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
