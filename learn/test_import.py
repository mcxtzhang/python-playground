#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import special_indicator
import os

print sys.path
#sys.path.append('/Users/zhangxutong/py/python-playground')
sys.path.append('../../python-playground')

from learn.sub.sub_module_file import SubModuleClass

sub = SubModuleClass()
sub.func()


#一个大坑， python的包要求包下必须有一个__init__.py文件，  否则导入其他包会报错。


print os.getcwd()

print special_indicator.getSeparator()