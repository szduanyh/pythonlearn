# -*- coding: utf-8 -*-
__author__ = 'admin-1'


class Employee:
    'Common base class for all employee'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmplyee(self):
        print 'Name :', self.name, ', Salary:', self.salary


emp1 = Employee('Zara', 2000)
emp2 = Employee('Manni', 5000)

emp1.displayEmplyee()
emp2.displayEmplyee()

print 'Total Employee %d' % Employee.empCount

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
