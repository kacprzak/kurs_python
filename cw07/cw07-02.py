#!/usr/bin/env python3
# cw07-02

from math import sqrt
import sys

print('Program obliczający pierwiastki równania kwadratowego.')

if len(sys.argv) < 4:
    print('Sposób użycia: {} a b c'.format(sys.argv[0]))
    sys.exit()

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
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
    print('Obliczone pierwiastki to:')
    print(' x1 = {0:.2f}, x2 = {1:.2f}'.format(x1, x2))
elif delta < 0:
    print('Równanie nie posiada rozwiązań')
else:
    x = -b/(2*a)
    print('Równanie ma jedno rozwiązanie:')
    print(' x = {0:.2f}'.format(x))
