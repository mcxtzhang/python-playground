#!/usr/bin/python
# -*- coding: UTF-8 -*-

# elif 是 else if 的缩写
# 注意冒号 和缩进
age = 12;
if age > 18:
    print 'adult'
elif age > 6:
    print 'teenager'
else:
    print 'child'

# 循环
sum = 0
for x in range(1, 101):
    print x
    sum = sum + x
print sum

# while

sum = 0;
n = 99;
while n > 0:
    sum += n;
    n = n - 2;
print sum
