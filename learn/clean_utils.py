#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

directorys = ["../logs","../output"]
for i,directory in enumerate(directorys):
    #print directory
    if os.path.isdir(directory):
        fileList = os.listdir(directory)
        for fileName in fileList:
            try:
                os.remove(directory+"/"+fileName)
            except:
                print "s.remove(%s+"/"+%s)  error!"%(directory,fileName)
    else:
        print "%s is not directory" %directory