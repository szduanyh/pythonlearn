__author__ = 'dyh'
# -*- coding: utf-8 -*-

# 大括号或set() 函数可以用来创建集合。注意：想要创建空集合，你必须使用set()而不是{}。后者用于创建空字典，
basket = {'apple', 'orange', 'apple', 'pear'}
print(basket)

print('apple' in basket)

a = set('abcd')
b = set('cdefg')
print(a)
print(b)
# letters in either a or b
print(a | b)
# letters in both a and b
print(a & b)
# letters in a or b but not both
print(a ^ b)
