#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math

__author__ = 'dyh'

print("My name is %s and weight is %d kg!" % ('Zara', 21))

a = [-1, 2, 3, 4, 5, 666, 77, 123, 232.23]
del a[0]

print(a)

del a[2:4]
print(a)

print(math.exp(1))

var = 0
while var < 50:
    print(random.choice(range(10)))
    var += 1

print("--------------------------")
while var < 100:
    print(random.uniform(1, 10))
    var += 1
