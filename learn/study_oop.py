#!/usr/bin/python
# -*- coding: UTF-8 -*-
def func1(obj):
    obj.func2()


class C1:
    def func2(self):
        print "I am C1 func2"


class C2:
    def func2(self):
        print "I am C2 func2"


c1 = C1()
c2 = C2()
func1(c1)
func1(c2)
