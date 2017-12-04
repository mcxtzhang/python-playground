#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错
import collections

L = ['Hello', 'World', 18, 'Apple', None]

result = [s.lower() for s in L if isinstance(s, str)]
print result
