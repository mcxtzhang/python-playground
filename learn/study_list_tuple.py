#!/usr/bin/python
# -*- coding: UTF-8 -*-

a_list = ['a','b','c']
print a_list

print len(a_list)

#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print a_list[-1]

# 倒数第二个
print a_list[-2]

#add元素：append()
a_list.append('d')
print a_list

# 指定插入位置 : insert()
a_list.insert(2,'2')
print a_list

# 删除末尾元素，用pop（）
del_ele = a_list.pop()
print del_ele
print a_list

#删除指定位置 用 pop(i),
del_ele = a_list.pop(2)
print del_ele
print a_list


# 元素类型可以不同
list2 = ['a',1,True]
print list2

list2 = ['a',1,['sub1','sub2'],True]
print list2
print len(list2)




#  tuple 和list 类似，但是tuple不可变。没有append insert,用()定义
a_tuple = (1,2,3)
print a_tuple
a_tuple = (1)
print a_tuple
#   定义只有一个元素的tuple时，必须加一个 逗号，
a_tuple = (1,)
print a_tuple
