#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 默认参数,默认的参数最好是不可变对象，以免多次调用，改变了值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print power(10)
print power(10, 3)


# 可变参数： 一个*


# 关键字参数 ，允许输入0个或任意个含参数名的参数。（key=value,...）内部组装成一个dict
def persion(name, age, **kw):
    print ('name', name, 'age:', age, 'other:', kw)


persion('Michael', 30)

persion('mcxtzhang', 26, job="RD")

persion('vicky', 24, sex="female", city="SH")


# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product2(x, y):
    return x * y


def product(*params):
    if len(params) <= 0:
        raise TypeError("params length can not be 0")
    result = 1
    for p in params:
        result = result * p
    return result


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        print product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

import math


def quadratic(a, b, c):
    x1 = float(-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
    x2 = float(-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
    return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print (a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print (a, '-->', c)
        move(n - 1, b, a, c)

move(3,'A',"B",'C')