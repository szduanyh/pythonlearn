#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'dyh'

squares = [x ** 2 for x in range(10)]
print(squares)

L = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]
print(L)

vec = [-4, -2, 0, 2, 4]

# create a new list with the values double
print([x * 2 for x in vec])

# filter the list to exclude negative number
print([x for x in vec if x >= 0])

# applay a function to all elements
print([abs(x) for x in vec])

vec2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec2 for num in elem])
