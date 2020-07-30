#!/usr/bin/python
# -*- coding: UTF-8 -*-
import subprocess
import commands

import re

# s_men = ".".join(output) # 转换为string
# print(s_men)
# men2 = int(re.findall("TOTAL.(\d+)*", s_men, re.S)[0])
# print(men2 )
import time

import os

__scheme = "dianping://feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=d6a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"

__scheme = "dianping://router_feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=d6a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"

cmd = "adb shell am start -a android.intent.action.VIEW -d \"%s\"" % (__scheme)

# s, output = commands.getstatusoutput(
#     "adb shell am start -a android.intent.action.VIEW -d \"%s\"" % (
#         __scheme))
# print output

os.system(cmd)
