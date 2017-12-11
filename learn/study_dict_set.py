#!/usr/bin/python
# -*- coding: UTF-8 -*-
# dict
d = {'a': 1, 'b': 2, 'c': 3}
#print d['tan90']
print d['a']

# 通过 in 判断key是否存在
print 'd' in d

print 'c' in d

# 通过get 取值，不存在返回None
value = d.get('e')
print d.get('d')
if value is None:
    print 'bucunzai'


# 删除 pop(key)
value = d.pop('b')
print value
print d



########set

#用set(list)定义，set中不包含重复元素，创建set需要提供一个list
s = set([1,1,2,2,3,3])

print s

# add(key) 添加
s.add(4)
print s

# remove(key)删除
s.remove(4)
print s

#set 可以作为数学上的无序／无重复元素集合，因此可以做 交集并集 等
s1 = set([1,2,3,4])
s2 = set([2,3,5])
print s1&s2
print s1|s2





#tuple 放入 dict set 中


