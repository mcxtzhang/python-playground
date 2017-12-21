#!/usr/bin/python
# -*- coding: UTF-8 -*-

def compare_func(x1, x2):
    x1 = x1.upper()
    x2 = x2.upper()
    if x1 > x2:
        return 1
    if x2 > x1:
        return -1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], compare_func)
