#!/usr/bin/env python3
# cw07-04

values = []

with open('dane.txt', 'r') as f:
    for line in f:
        try:
            values.append(int(line))
        except:
            pass

print('Największa odczytana liczba to:', max(values))

