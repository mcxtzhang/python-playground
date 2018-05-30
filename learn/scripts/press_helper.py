#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands

import time

while True:
    #time.sleep(1)
    commands.getoutput("adb shell input tap 200 200")
