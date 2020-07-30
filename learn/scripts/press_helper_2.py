#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands

import time

device_name = "cd78b9ab"
device_name = "emulator-5554"
while True:
    # time.sleep(1)
    # commands.getoutput("adb shell input tap 600 1900")
    # time.sleep(3)
    # commands.getoutput("adb shell input tap 700 1591")
    # time.sleep(3)



    #commands.getoutput("adb -s %s shell input tap 407 2020" % device_name)
    commands.getoutput("adb -s %s shell input tap 448 1392" % device_name)
    print "开始战斗"
    time.sleep(30)
    #commands.getoutput("adb -s %s shell input tap 628 1850" % device_name)
    commands.getoutput("adb -s %s shell input tap 456 1291" % device_name)
    print "重新战斗"
    time.sleep(2.5)

    #commands.getoutput("adb -s %s shell input tap 900 1650" % device_name)
