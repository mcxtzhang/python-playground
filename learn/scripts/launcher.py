#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 确保进程的存在
import commands

import re

scheme = ""
s, o = commands.getstatusoutput("adb shell am start -a android.intent.action.VIEW -d %s" % scheme)
print s
print o
