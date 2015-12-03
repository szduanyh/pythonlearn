__author__ = 'dyh'
# -*- coding: utf-8 -*-

print('hello 你好！')

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# print the length of list
print(len(classmates))

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1])

# 以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-2])
print(classmates[-3])

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Jack')
print(classmates)

classmates.insert(1, 'Tom')
print(classmates)

classmates.pop(0)
print(classmates)

# tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
teachers = ('Michael', 'Bob', 'Tracy')
print(teachers)
