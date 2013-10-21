#!/usr/bin/env python3
# cw07-01

import sys
from math import factorial

if len(sys.argv) < 2:
    print('Nie podano argumentu!')
    sys.exit()

try:
    n = int(sys.argv[1])
except ValueError:
    print('Argument nie jest liczbą całkowitą!')
    sys.exit()

try:
    print('{}! = {}'.format(n, factorial(n)))
except ValueError:
    print('Argument nie może być mniejszy od zera!')



