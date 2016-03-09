#!/usr/bin/python
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print(L[0:3])
# 如果第一个索引是0，还可以省略：
print(L[:3])

print(L[1:3])

print(L[-2:])
print(L[-2:-1])

L2 = list(range(100))
print(L2[0:10])
print(L2[-10:])

print(L2[0:10:2])

print(L2[::2])
print(L2[::5])

print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
