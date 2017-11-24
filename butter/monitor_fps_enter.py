#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands
import sys

import os

from stuff_file_utils import stuff_file

configFilePath = sys.argv[1]
config_file = open(configFilePath)

# todo 正式使用记得删除
stuff_file.clean_dirs()

while 1:
    line = config_file.readline()
    if not line:
        break
    pass
    print line
    # commands.getstatusoutput("monitor.sh)
    # (status,output)=commands.getstatusoutput("./monitor.sh %s" %line)
    # print output
    os.system("./start_activity.sh %s" % line)
