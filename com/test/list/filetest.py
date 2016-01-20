# -*- coding: utf-8 -*-
__author__ = 'admin-1'

# 打开一个文件
fo = open("d:/foo.txt", "a+")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace

fo.write("Python is a gread language!\nYeah,it is great!!!\n")
fo.close()
