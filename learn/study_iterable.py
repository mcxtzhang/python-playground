#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 判断一个对象是否 可迭代  ，通过colections模块的iterable类型判断
from collections import Iterable

print isinstance('abc', Iterable)
print isinstance(2, Iterable)
print isinstance((1, 23, 4), Iterable)

# dict的迭代,得到的是key
mapping = {'name': 'zhangxutong', 'sex': 1, "skill": (1, 2, 3)}
for item in mapping:
    print item

for value in mapping.values():
    print value

for k,v in mapping.items():
    print ("key:%s,value:%s"%(k,v))
