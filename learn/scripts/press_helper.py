#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands

import time

while True:
    #time.sleep(1)
    # commands.getoutput("adb shell input tap 600 1900")
    # time.sleep(3)
    # commands.getoutput("adb shell input tap 700 1591")
    # time.sleep(3)
    commands.getoutput("adb shell input tap 616 2078")
    print "开始战斗"
    time.sleep(35)
    commands.getoutput("adb shell input tap 628 1850")
    print "重新战斗"
    time.sleep(2.5)
