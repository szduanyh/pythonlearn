# -*- coding: utf-8 -*-
__author__ = 'dyh'


L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)


# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)
