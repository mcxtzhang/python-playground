#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands
import json
import sys

import os

from stuff_file_utils import stuff_file

#configFilePath = sys.argv[1]
configFilePath = "./monitor_fps.config"
config_file = open(configFilePath)

# todo 正式使用记得删除
stuff_file.clean_dirs()


def shellquote(s):
    """
    转义字符串
    """
    return """+s+""" + s.replace("'", "'\\''") + "'"


s = "a&a"
print "特殊字符:%s" % s

while 1:
    line = config_file.readline()
    if not line:
        break
    pass
    print line
    obj = json.loads(line)
    scheme = obj['scheme'].encode('utf-8')
    print scheme
    # commands.getstatusoutput("monitor.sh)
    # (status,output)=commands.getstatusoutput("./monitor.sh %s" %line)
    # print output



    # os.system("./start_activity.sh %s" % scheme)

    # scheme  = shellquote(scheme)

    cmd = "adb shell am start -a android.intent.action.VIEW -d \"%s\"" % scheme
    print "命令:%s"%cmd

    s, o = commands.getstatusoutput(cmd)
    print s
    print o


    # os.subprocess.call("adb shell am start -a android.intent.action.VIEW -d %s" % scheme, shell=True)
