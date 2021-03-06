#!/usr/bin/python
# -*- coding: UTF-8 -*-
def now():
    print '2017-12-14'


f = now
f()

print now.__name__
print f.__name__


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)

        return wrapper

    return decorator


@log('zhixing')
def func2():
    print "func2"


func2()
