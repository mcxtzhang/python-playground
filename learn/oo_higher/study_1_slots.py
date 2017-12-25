#!/usr/bin/python
# -*- coding: UTF-8 -*-
# __slots__ 是 限制给类动态添加 属性、方法的关键字
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = "mcxtzhang"
print s.name


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s, Student)

s.set_age(25)
print s.age

# 给一个实例绑定的方法，其他实例是不能用的，
# 为了所有的实例都能用，可以给class绑定方法

Student.set_age = MethodType(set_age, None, Student)
s2 = Student()
s2.set_age(100)
print s2.age


# 通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现

# 使用__slots__ 限制class的属性 (方法好像不能限制 只能限制属性)
class Teacher(object):
    __slots__ = ('name', 'age')

    def __init__(self):
        self.sex = "man"


def set_age(self, age):
    self.age = age


t = Teacher()
Teacher.set_age = MethodType(set_age, None, Teacher)
t.set_age(26)
print t.age

# __slots__ 限制了 导致出错
print t.sex
