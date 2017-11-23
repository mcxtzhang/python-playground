# -*- coding: UTF-8 -*-
import commands
import sys
import time

import LogHandler

print "begin start activity...."
scheme = sys.argv[1]
# scheme = "dianping://cinemalist"
print "参数是" + scheme
(status, output) = commands.getstatusoutput("adb shell am start -a android.intent.action.VIEW -d %s" % (scheme))
print status
print output
time.sleep(5)

logHandler = LogHandler.LogHandler(scheme)
# 后期可配置
for num in range(0, 4):
    print "begin swipe...."
    # 滑动策略后期可能会变
    commands.getstatusoutput("adb shell input swipe 800 800 200 200")
    # print status
    # print output
    print "begin dumpsys and save to file: logs/log%s" % num
    (status, output) = commands.getstatusoutput(
        "adb shell dumpsys gfxinfo com.dianping.v1 reset framestats > logs/log%s" % num)
    # 处理文件
    if num == 0:
        logHandler.handleLog("logs/log%s" % num)
    else:
        logHandler.mergeLog("logs/log%s" % num)
        # print status
        # print output

# 输出文件
logHandler.outputFile()