#!/usr/bin/env python3
# cw06-03

from math import sqrt
import sys

print('Program obliczający pierwiastki równania kwadratowego.')

repeat = 't'

while repeat == 't':
  
    a = input('Podaj a: ')
    b = input('Podaj b: ')
    c = input('Podaj c: ')

    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print('Jedna z wartości nie jest liczbą!')
        sys.exit()

    if a == 0:
        print('To nie jest równanie kwadratowe!')
        sys.exit()

    print('Dla równania kwadratowego o współczynnikach:')
    print(' a = {0}, b = {1}, c = {2}'.format(a, b, c))

    delta = b*b - 4*a*c

    if delta > 0:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        print('Obliczone pierwiatki to:')
        print(' x1 = {0:.2f}, x2 = {1:.2f}'.format(x1, x2))
    elif delta < 0:
        print('Równanie nie posiada rozwiązań')
    else:
        x = -b/(2*a)
        print('Równanie ma jedno rozwiązanie:')
        print(' x = {0:.2f}'.format(x))

    repeat = input("Powtórzyć obliczenia [t/n]: ").strip()
