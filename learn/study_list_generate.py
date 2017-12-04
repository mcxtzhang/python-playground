#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 强大的创建List的生成式

# 生成1*1, 2*2.......
temp = [x * x for x in range(1, 11)]
print temp

# 后面可以加上判断过滤条件
temp = [x * x for x in range(1, 11) if x % 2 == 0]
print temp

# 两层循环
temp = [m + n for m in 'ABC' for n in 'XYZ']
print temp

# 列出当前目录下  所有文件和目录名:
import os

temp = [d for d in os.listdir('.')]
print temp

# for循环可以同时使用多个变量 2+。比如dict的items()
d = {"x": 'A', "y": 'B', "z": 'C'}
temp = [m + "=" + n for m, n in d.items()]
print temp


# 把一个List中所有字符串小写
L = ['Hello', 'World', 'IBM', 'Apple']
temp = [s.lower() for s in L]
print temp