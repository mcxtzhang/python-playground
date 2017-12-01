#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 利用切片 实现一个trim()
def trim(s):
    begin = 0
    for i in range(len(s)):
        if s[i] == ' ':
            begin = i + 1
        else:
            break

    end = len(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            end = i
        else:
            break
    return s[begin:end]


# 测试:
print trim('hello  ')
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
