#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 确保进程的存在
import commands

import re

pkg_name = "com.dianping.v1"
o = commands.getoutput("adb shell ps | grep %s$" % (pkg_name))
temp_list = re.split("\s+", o)
print "shell ps | grep %s result:%s" % (pkg_name, temp_list)
if len(temp_list) > 2:
    pid = temp_list[1]
    print "pid:%s" % pid
    s, o = commands.getstatusoutput("adb shell am force-stop %s" % (pkg_name))
    print s
    print o
