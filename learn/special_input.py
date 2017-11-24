#!/usr/bin/python
# -*- coding: UTF-8 -*-


import commands
import sys

scheme = sys.argv[1]
# scheme = "dianping://cinemalist"
# print "参数是" + scheme
command = r"adb shell am start -a android.intent.action.VIEW -d %s" % (scheme)
(status, output) = commands.getstatusoutput(command)
print status
print output