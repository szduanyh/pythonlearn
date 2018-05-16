#!/usr/bin/python
# -*- coding: utf-8 -*-

var1 = 100
var2 = 0

if var1:
    print("1 - if表达式条件为true")
    print(var1)

if var2:
    print("2 - if表达式条件为true")
    print(var2)

print("")
print("Good bye!")

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

print("")

age = int(input("请输入你家狗的年龄"))
if age < 0:
    print("你是逗我的吧！")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("对应人类年龄 ", human)
