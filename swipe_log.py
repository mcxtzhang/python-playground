# -*- coding: UTF-8 -*-
import commands
import sys

import time

import LogHandler

# print "begin start activity...."
from ZUtils import ZUtils

scheme = sys.argv[1]
# scheme = "dianping://cinemalist"
# print "参数是" + scheme
# (status, output) = commands.getstatusoutput("adb shell am start -a android.intent.action.VIEW -d %s" % (scheme))
# print status
# print output
# time.sleep(5)

logHandler = LogHandler.LogHandler(scheme)
# 后期可配置 循环次数
for num in range(0, 10):
    print "begin swipe...."
    # 滑动策略后期可能会变
    commands.getstatusoutput("adb shell input swipe 800 800 800 500")
    # print status
    # print output
    fileName = "logs/log_%s_%s" % (ZUtils.getTimeSuffix(), num)
    time.sleep(1)

    print "begin dumpsys and save to file:%s" % fileName
    (status, output) = commands.getstatusoutput(
        "adb shell dumpsys gfxinfo com.dianping.v1 reset framestats > %s" % fileName)

    # 处理文件
    if num == 0:
        logHandler.handleLog("%s" % fileName)
    else:
        logHandler.mergeLog("%s" % fileName)
    # print status
    # print output


# 输出文件
logHandler.outputFile()
