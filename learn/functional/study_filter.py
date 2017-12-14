#!/usr/bin/python
# -*- coding: UTF-8 -*-
print filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# 练习

# 请尝试用filter()删除1~100的素数。
import math


def isPrimNum(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


print filter(isPrimNum, range(1, 101))
