#!/usr/bin/python
# -*- coding: utf-8 -*-

L = [1, 2, 8, 6, 74, 12, -98, -7, -8, 66]
L2 = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(L))

print(sorted(L, reverse=True))

print(sorted(L, key=abs))

print(sorted(L2))

print(sorted(L2, key=str.lower))
