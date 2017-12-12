#!/usr/bin/python
# -*- coding: UTF-8 -*-
class MemoryModel(object):
    def __init__(self, pkg_name="", heap_size="", heap_alloc="", heap_free="", rate=""):
        self.pkg_name = pkg_name
        self.heap_size = heap_size
        self.heap_alloc = heap_alloc
        self.heap_free = heap_free
        self.rate = rate


import json


# 自定义类
class MyClass:
    # 初始化
    def __init__(self):
        self.__a = 2
        self.__b = 'bb'

        ##########################


# 创建MyClass对象
myClass = MyClass()
# 添加数据c
myClass.c = 123
myClass.__a = 3
# 对象转化为字典
myClassDict = myClass.__dict__
# 打印字典
print (myClassDict)
# 字典转化为json
myClassJson = json.dumps(myClassDict)
# 打印json数据
print (myClassJson)

model = MemoryModel(1,
                    "%.2f" % (float(1) / 1024),
                    "%.2f" % (float(1) / 1024),
                    "%.2f" % (float(1) / 1024),
                    "%.2f" % (float(1) / 1024 / float(2)))
str_json_model = json.dumps(model.__dict__)
print str_json_model
print type(str_json_model)
print isinstance(str_json_model, str)

# 还原的过程，将json字符串还原成dict或者对象
json_obj_model = json.loads(str_json_model)
# dict
print json_obj_model
print type(json_obj_model)

# 对象
new_obj =  MemoryModel()
new_obj.__dict__ = json_obj_model
print json.dumps(new_obj.__dict__)

