#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

print(list(range(1, 11)))

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

L = ['Hello', 'World', 'IBM', 'Apple']

print([x.lower() for x in L])
print([x.upper() for x in L])

L2 = ['Hello', 'World', 18, 'Apple', None]

print([x.lower() for x in L2 if isinstance(x, str)])
