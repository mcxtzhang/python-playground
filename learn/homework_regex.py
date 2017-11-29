#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

email1 = "someone@gmail.com"
email2 = "bill.gates@microsoft.com"
regex_email = r'^([0-9a-zA-Z.]+)@([0-9a-zA-Z]+).([0-9a-zA-Z]+)'
print re.match(regex_email, email1).groups()
print re.match(regex_email, email2).groups()









# 版本二可以验证并提取出带名字的Email地址：
#
# <Tom Paris> tom@voyager.org
