#!/usr/bin/env python3
# cw06-01

from math import sqrt

a = 2
b = 1
c = -2

print('Dla równania kwadratowego o współczynnikach:')
print(' a = {0}, b = {1}, c = {2}'.format(a, b, c))

delta = b*b - 4*a*c # 17

if delta > 0:
    x1 = (-b - sqrt(delta))/(2*a) # -1.28
    x2 = (-b + sqrt(delta))/(2*a) # 0.78
    print('Obliczone pierwiatki to:')
    print(' x1 = {0:.2f}, x2 = {1:.2f}'.format(x1, x2))
elif delta < 0:
    print('Równanie nie posiada rozwiązań')
else:
    x = -b/(2*a)
    print('Równanie ma jedno rozwiązanie:')
    print(' x = {0:.2f}'.format(x))
