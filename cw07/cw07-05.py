#!/usr/bin/env python3
# cw07-05

values = []

with open('dane.txt', 'r') as f:
    for line in f:
        try:
            values.append(int(line))
        except:
            pass

print('Najmniejsza odczytana liczba to:', min(values))

