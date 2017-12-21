#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 返回函数
def lasy_sum(*args):
    def sum():
        result = 0;
        for n in args:
            result = result + n
        return result

    return sum


print lasy_sum(1, 2, 3)()


# 另一个值得注意的：返回的函数并没有立刻执行，而是直到调用了f()才执行：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print f1()
print f2()
print f3()

# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：

print "解决办法就是嵌套一个函数，并在嵌套的函数里 使用到参数"


def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print f1()
print f2()
print f3()
