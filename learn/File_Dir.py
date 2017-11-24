#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# print os.name
# print os.uname()
# #环境变量
# print  os.environ

# 查看 创建 删除 目录：
# 查看
curPath = os.path.abspath('.')
print curPath

# 在将两个路径合成一个时， 不要直接拼接字符串，要使用os.path.join()函数 返回的结果。 因为 不同的系统，路径分隔符不一样，mac：/   wind:\
newPath = os.path.join(curPath, "newdir")
print newPath

# os.mkdir(newPath)
# os.rmdir(newPath)

# 同样，拆分路径时，也不要直接去拆字符串，要利用os.path.split()函数， 可以把路径拆为两部分， 后一部分时最后级别的目录或文件名：
splitResult = os.path.split(newPath)
print splitResult

newFilePath = os.path.join(curPath, "newFile.txt")
print newFilePath
splitResult = os.path.split(newFilePath)
print splitResult

# os.path.splitext() 可以直接获得 文件扩展名
print os.path.splitext(newFilePath)

# 重命名 os.rename()
# os.rename('2.py', 'tobedele')

toDelPath = os.path.join(os.path.abspath('.'), 'tobedele')
splitResult = os.path.splitext(toDelPath)
print splitResult

# 删除
# os.remove(toDelPath)

# 列出目录下所有目录文件
allFile = [x for x in os.listdir('.') if os.path.isdir(x)]
print allFile

# 所有文件 目录
allFile = [x for x in os.listdir('.')]
print allFile

# 所有py文件
allFile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print allFile
