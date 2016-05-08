#!/usr/bin/python
# -*- coding: utf-8 -*-

def f(x):
    return x * x


li = [x for x in range(1, 11)]

r = map(f, li)
print(list(r))

lis = list(map(str, list(x for x in range(11))))
print(lis)
