#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 为了让使用时，和属性一样的简单。 同时具有 安全检查等功能，可以使用@property注解
class Student(object):
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0~100!")
        self.__score = value


s = Student()
s.score = 60
print s.score


# s.score = 1000
# print s.score


# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Teacher(object):
    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2017 - self.__birth


t = Teacher()
t.birth = 1991
print t.birth
print t.age

#t.age = 10
