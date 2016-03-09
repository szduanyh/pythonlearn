#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Iterable

print(isinstance('abc', Iterable))

print(isinstance(123, Iterable))

print(isinstance([1, 2, 3], Iterable))
