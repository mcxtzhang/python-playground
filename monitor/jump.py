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

for i in range(0, 1):


    __scheme = "dianping://router_feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=d1a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"
    __scheme = "dianping://feeddetail?type=1&mainid=529445461&queryid=b18d0309-990b-43bb-900a-1ec4902cbd24&styletype=1&norecommend=1"
    # s, output = commands.getstatusoutput(
    #     "adb shell am start -W -a android.intent.action.VIEW -d \"%s\"" % (
    #         __scheme))
    s, output = commands.getstatusoutput(
        "adb shell am start \"%s\"" % (
            __scheme))
    time.sleep(1)
    print output
