#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
import commands

import re

pkg_name = "com.dianping.v1"
#pkg_name = "com.xingin.xhs"
cmd = "adb shell  dumpsys  meminfo %s" % (pkg_name)
print(cmd)

output = commands.getoutput(cmd)#.split()
print output

# s_men = ".".join(output) # 转换为string
# print(s_men)
# men2 = int(re.findall("TOTAL.(\d+)*", s_men, re.S)[0])
# print(men2 )