#!/usr/bin/env python3
# cw07-03

from math import sqrt
import sys

print('Program obliczający pierwiastki równania kwadratowego.')
print('Wyniki zostaną zapisane w pliku output.txt.')

with open('output.txt', 'w') as out_f:
    with open('cw07-03.txt', 'r') as f:
        for line in f:
            cols = line.strip().split()

            if len(cols) < 3:
                continue

            try:
                a = float(cols[0])
                b = float(cols[1])
                c = float(cols[2])
            except ValueError:
                print('Jedna z wartości nie jest liczbą!')
                sys.exit()

            if a == 0:
                print('To nie jest równanie kwadratowe!')
                sys.exit()

            delta = b*b - 4*a*c

            if delta > 0:
                x1 = (-b - sqrt(delta))/(2*a)
                x2 = (-b + sqrt(delta))/(2*a)
                out_f.write('{0:.2f} {1:.2f}\n'.format(x1, x2))
            elif delta < 0:
                # Przy braku rozwiązań wstaw pusty wiersz
                out_f.write('\n')
            else:
                x = -b/(2*a)
                out_f.write('{0:.2f}\n'.format(x))

