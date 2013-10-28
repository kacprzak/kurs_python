#!/usr/bin/env python3
# cw08-04

def suma(tab):
    return sum(tab)

def srednia_arytmetyczna(tab):
    return sum(tab) / len(tab)

def srednia_geometryczna(tab):
    result = 1
    for element in tab:
        result *= element
    return result ** (1/len(tab))


filename = 'dane.txt'
values = []

with open(filename, 'r') as f:
    for line in f:
        try:
            values.append(int(line))
        except:
            pass

print('Wczytano', len(values), 'liczb z pliku', filename)

print('Suma:', suma(values))
print('Średnia arytmetyczna:', srednia_arytmetyczna(values))
print('Średnia geometryczna:', srednia_geometryczna(values))
