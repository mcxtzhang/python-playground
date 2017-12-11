#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands

(s,o)= commands.getstatusoutput("adb shell dumpsys gfxinfo com.dianping.v1 reset framestats")
print s
print o