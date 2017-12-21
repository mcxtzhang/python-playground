#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 高阶函数
print abs
f = abs
print f(-100)


# 传入函数

def add(x, y, f):
    return f(x) + f(y)


print add(1, -1, abs)


# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
def f(x):
    return x * x


# 使用map 直观。你能一眼知道，要把 函数f应用在 list的每一个元素上，并把结果生成一个新的list
print map(f, range(1, 10))


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x, y):
    return x + y


print reduce(add, range(1, 101))


# 把 [1 ,3,5,7,9]=>13579
def append(x, y):
    return x * 10 + y


print reduce(append, [1, 3, 5, 7, 9])


# str -》int
def fn(x, y):
    return x * 10 + y


def char2num(c):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]


print reduce(fn, map(char2num, "123456"))


# 整理成函数就是
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    return reduce(fn, map(char2num, s))


print str2int("1234567890")


# 配合lambda:
def str2int(s):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]

    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print str2int("123333")

#  练习 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
print "练习时间到:"


def format_1(input_list):
    def normalize(name):
        name = name[0].upper() + name[1:].lower()
        return name

    return map(normalize, input_list)


print format_1(['adam', 'LISA', 'barT'])

print "第二题："


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(list):
    return reduce(lambda x1, x2: x1 * x2, list)


print prod([1, 2, 3, 4, 5])
