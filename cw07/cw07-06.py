#!/usr/bin/env python3
# cw07-06

values = []

with open('dane.txt', 'r') as f:
    for line in f:
        try:
            values.append(int(line))
        except:
            pass

print(values)

change = True

for i in range(0, len(values) - 1):
    change = False
    for k in range(0, len(values) - 1 - i):
        if values[k+1] < values[k]:
            values[k], values[k+1] = values[k+1], values[k]
            change = True
    if not change:
        break

print(values)
values.reverse()
print(values)
        
