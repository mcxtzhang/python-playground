#!/usr/bin/python
# -*- coding: UTF-8 -*-

#  正则表达式
import re

s = "ABC\\-001"
# 对应ABC\-001
s = r"ABC\-001"
# 对应ABC\-001

# 判断是否匹配
result = re.match(r"^\d{3}-\d{3,8}$", "010-12345")
print result
result = re.match(r"^\d{3}-\d{3,8}$", "010 12345")
print result

# 常见判断方式
if re.match(r'^\d{3}\+\d{11}$', "086+18616320845"):
    print "match"
else:
    print "gun"

# 重点  切分字符串， 用正则表达式切分字符串 比固定的字符更灵活
str = "a b   c"  # 三个空格
print str.split(" ")

print re.split('\s+', str)

# 用 ， 或者  空格  分隔
print re.split('[\s\,]+', "a b    c, d  , e")


# 分组 用 （） 表示的就是要提取的分组
m = re.match(r'^(\d{3})-(\d{3,8})$',"010-123456")
print m
print m.group(0)
print m.group(1)
print m.group(2)


# 贪婪匹配  正则默认是贪婪匹配，会匹配尽可能多的字符
print re.match(r'^(\d+)(0*)$','102300').groups()
#('102300', '')

# 加上? 让其采用非贪婪匹配
print re.match(r'^(\d+?)(0*)$','102300').groups()


#编译 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式
regex_telphone = re.compile(r'^(\d{0,3})-(\d{3,8})$')
print regex_telphone.match("010-123456").groups()
print regex_telphone.match("010-8086").groups()