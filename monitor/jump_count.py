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

count = 0
while True:
    __scheme = "dianping://router_feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=16a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"
    __scheme = "dianping://feeddetail?type=1'&'mainid=451230597'&'styletype=1'&'queryid=16a7bed0-67d5-4f45-a021-7d0169ae29a9'&'videosrc=home_feed"
    s, output = commands.getstatusoutput(
        "adb shell am start -W -a android.intent.action.VIEW -d \"%s\"" % (
            __scheme))
    time.sleep(1)
    print s
    print output
    if s == 0:
        count = count + 1
    else:
        break
print "一共跳转成功了%s次" % (count)


class JumpLimitTester:
    def __init__(self, _scheme):
        self.__scheme = _scheme;

    def test(self):
        pass

    def jump