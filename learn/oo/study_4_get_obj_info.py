#!/usr/bin/python
# -*- coding: UTF-8 -*
print type(123)
print type('str')
print type(None)
print type(abs)


class Person:
    def __init__(self):
        pass

    def wentibuda(self):
        print "wentibuda  yiqie huihao de"


person = Person()
print type(person)
p = Person
print type(p)

print type(Person)

print type(int)
print type(str)

print type(int) == type(str)

# 获取一个对象的 所有属性和方法，可以用dir(),它返回一个字符串List
print dir(Person)
print dir(person)

print dir("abc")


#  配合 getattr() setattr() hasattr() 可以直接操作一个对象的状态:
class MyObject(object):
    def __init__(self):
        self.__x = 9
        self.y = 10

    def power(self):
        return self.__x * self.__x


obj = MyObject()

print dir(MyObject)
print "X:"
print hasattr(obj, "__x")  ## 私有属性找不到
print hasattr(obj, "_MyObject__x")  ## 要使用这种方式才能找到 但是不推荐
print "Y:"
print hasattr(obj, "y")

print "Z:"
print hasattr(obj, "z")
setattr(obj, "z", 11)
print hasattr(obj, "z")
print getattr(obj, "z")

print "a:"
# print getattr(obj,"a")
print getattr(obj, "a", 1)

print "power:"
print  hasattr(obj, "power")
f_power = getattr(obj, "power")
print f_power
print f_power()


def exec_power(obj):
    if hasattr(obj, "power"):
        print obj.power()
    else:
        print "the obj:%s do not has func:power()" % obj


exec_power(obj)
exec_power(f_power)
