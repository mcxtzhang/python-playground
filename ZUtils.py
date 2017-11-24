#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os


class ZUtils:
    '工具类'

    @staticmethod
    def getTimeSuffix():
        return "%s" % (time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())))

    @staticmethod
    def cleanCache():
        directorys = ["./logs", "./output"]
        for i, directory in enumerate(directorys):
            # print directory
            if os.path.isdir(directory):
                fileList = os.listdir(directory)
                for fileName in fileList:
                    try:
                        os.remove(directory + "/" + fileName)
                    except:
                        print "s.remove(%s+" / "+%s)  error!" % (directory, fileName)
            else:
                print "%s is not directory" % directory
