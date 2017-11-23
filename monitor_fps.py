#!/usr/bin/python
# -*- coding: UTF-8 -*-
import commands
import sys

import os

configFilePath = sys.argv[1]
file = open(configFilePath)

while 1:
    line = file.readline()
    if not line:
        break
    pass
    print line
   # commands.getstatusoutput("monitor.sh)
    #(status,output)=commands.getstatusoutput("./monitor.sh %s" %line)
    #print output
    os.system("./start_activity.sh %s" %line)
