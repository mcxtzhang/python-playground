# -*- coding: UTF-8 -*-
import commands
import sys
import time

import LogHandler
# print "begin start activity...."
from ZUtils import ZUtils
from stuff_file_utils import stuff_file

scheme = sys.argv[1]
# scheme = "dianping://cinemalist"
# print "参数是" + scheme
# (status, output) = commands.getstatusoutput("adb shell am start -a android.intent.action.VIEW -d %s" % (scheme))
# print status
# print output
# time.sleep(5)

stuff_file.create_dirs()
logHandler = LogHandler.LogHandler(scheme)
# 后期可配置 循环次数 ,多加m次 作为log的补偿，只dump gfxinfo ，不 swipe。防止swipe后，log没有统计完全。
loop_count = 5
m = 1
for num in range(0, loop_count + m):
    print "begin swipe...."
    # 滑动策略后期可能会变
    if num < loop_count:
        commands.getstatusoutput("adb shell input swipe 800 800 800 500")
    # print status
    # print output

    # 休眠1s 尽量保证滑动结束
    time.sleep(1)

    fileName = "%s/log_%s_%s" % (stuff_file.get_stuff_dir(),ZUtils.getTimeSuffix(), num)

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
