#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

from ZUtils import ZUtils

KEY_BEGIN = "Profile data in ms:"
KEY_END = "View hierarchy:"

KEY = "---PROFILEDATA---"
KEY_FRAME_COMPLETE = "FrameCompleted,";


class LogHandler:
    '初步处理原始log，剔除无用信息，且将多个log中的相同scheme／activitiy的log 合并'

    def __init__(self, scheme):
        # print "init with %s \n" % scheme
        self.scheme = scheme
        self.__fileStringMap = {}

    # 第一次处理log
    def handleLog(self, fileName):
        # print "handleLog with %s \n" % fileName
        file_object = open(fileName)
        try:
            fileString = file_object.read()
            fileString = self._removeUselessInfo(fileString)

            indexComplete = fileString.find(KEY_FRAME_COMPLETE)

            while indexComplete > -1:

                profileIndex = fileString.index(KEY);

                completeIndex = fileString.index(KEY_FRAME_COMPLETE) + len(KEY_FRAME_COMPLETE)
                secondProfileIndex = fileString.index(KEY, profileIndex + len(KEY))

                # print "completeIndex:%s"%completeIndex
                # print "secondProfileIndex:%s"%secondProfileIndex
                # print "profileIndex:%s"%profileIndex
                # print "len(KEY):%s"%len(KEY)
                # 没有fps数据的不写入文件
                if completeIndex + 1 != secondProfileIndex:
                    # 1 scheme信息
                    temp = self.scheme + "\n"

                    # 2 activity信息
                    activityInfo = fileString[0: profileIndex].strip()
                    temp = temp + activityInfo

                    # 3 fps info
                    temp = temp + fileString[completeIndex: secondProfileIndex].strip()
                    self.__fileStringMap[activityInfo] = temp

                # 截取 继续循环
                fileString = fileString[secondProfileIndex + len(KEY):]
                indexComplete = fileString.find(KEY_FRAME_COMPLETE)
                # print(temp)

        finally:
            file_object.close()

    def mergeLog(self, fileName):
        # print ("mergeLog with %s" % fileName)
        file_object = open(fileName)
        try:
            fileString = file_object.read()
            fileString = self._removeUselessInfo(fileString)

            indexComplete = fileString.find(KEY_FRAME_COMPLETE)

            while indexComplete > -1:
                profileIndex = fileString.index(KEY);

                completeIndex = fileString.index(KEY_FRAME_COMPLETE) + len(KEY_FRAME_COMPLETE)
                secondProfileIndex = fileString.index(KEY, profileIndex + len(KEY))

                # 没有fps数据的不写入文件
                if completeIndex + 1 != secondProfileIndex:
                    # 2 activity信息  和上面的差别 activityinfo 仅仅用来定位
                    activityInfo = fileString[0: profileIndex].strip()

                    # 3 fps info
                    temp = fileString[completeIndex: secondProfileIndex].strip()
                    self.__fileStringMap[activityInfo] = self.__fileStringMap[activityInfo] + temp

                # 截取 继续循环
                fileString = fileString[secondProfileIndex + len(KEY):]
                indexComplete = fileString.find(KEY_FRAME_COMPLETE)
                # print(temp)

        finally:
            file_object.close()

    # 一次task完成，输出n个file，每个file内是一个Activity的 fps info
    def outputFile(self):
        # 遍历字典列表
        i = 1
        for key, values in self.__fileStringMap.items():
            file_output = open(
                "output/monitor_result_%s_%s" % (ZUtils.getTimeSuffix(), i), 'w')
            file_output.write(values)
            file_output.close()
            i = i + 1

    def _removeUselessInfo(self, fileString):
        # remove useless log
        beginIndex = fileString.index(KEY_BEGIN) + len(KEY_BEGIN)
        endIndex = fileString.index(KEY_END)
        fileString = fileString[beginIndex:endIndex].strip()
        return fileString
