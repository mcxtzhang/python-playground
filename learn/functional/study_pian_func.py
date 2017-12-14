#!/usr/bin/python
# -*- coding: UTF-8 -*-
print int('12345')
print int('12345', base=8)

print int('1000', 2)


# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

def int2(x):
    return int(x, 2)


print int2('1')
print int2('10')

# functools.partial 就是帮助我们创建偏函数的。
import functools

int2 = functools.partial(int, base=2)
print int2('1')
print int2('10')

# 所以，简单总结functools.partial的作用就是，
##### 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。

# 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
print int2('10', base=10)

#创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
#上面相当于指定了kw
#下面相当于指定了args
print '指定偏函数的  args'
max10 = functools.partial(max,10)
print max10(1)
print max10(13,4)
print max10(1,5,6,7,8,8)
print max10(1,9,0)