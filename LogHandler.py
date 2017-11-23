#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time

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

    def handleLog(self, fileName):
        # print "handleLog with %s \n" % fileName
        file_object = open(fileName)
        try:
            fileString = file_object.read()
            # remove useless log
            beginIndex = fileString.index(KEY_BEGIN) + len(KEY_BEGIN)
            endIndex = fileString.index(KEY_END)
            fileString = fileString[beginIndex:endIndex].strip()

            # list = []

            indexComplete = fileString.find(KEY_FRAME_COMPLETE)

            while indexComplete > -1:

                profileIndex = fileString.index(KEY);
                # activity信息
                activityInfo = fileString[0: profileIndex].strip()
                temp = activityInfo

                completeIndex = fileString.index(KEY_FRAME_COMPLETE) + len(KEY_FRAME_COMPLETE)
                secondProfileIndex = fileString.index(KEY, profileIndex + len(KEY))

                # print "completeIndex:%s"%completeIndex
                # print "secondProfileIndex:%s"%secondProfileIndex
                # print "profileIndex:%s"%profileIndex
                # print "len(KEY):%s"%len(KEY)
                # 没有fps数据的不写入文件
                if completeIndex + 1 != secondProfileIndex:
                    temp = temp + fileString[completeIndex: secondProfileIndex]
                    self.__fileStringMap[activityInfo] = temp
                    # list.append(temp)

                # 截取 继续循环
                fileString = fileString[secondProfileIndex + len(KEY):]
                indexComplete = fileString.find(KEY_FRAME_COMPLETE)
                # print(temp)

        finally:
            file_object.close()

    def mergeLog(self, fileName):

        # print ("mergeLog with %s" % fileName)
        # print "handleLog with %s \n" % fileName
        file_object = open(fileName)
        try:
            fileString = file_object.read()
            # remove useless log
            beginIndex = fileString.index(KEY_BEGIN) + len(KEY_BEGIN)
            endIndex = fileString.index(KEY_END)
            fileString = fileString[beginIndex:endIndex].strip()

            indexComplete = fileString.find(KEY_FRAME_COMPLETE)

            while indexComplete > -1:

                profileIndex = fileString.index(KEY);
                # activity信息
                activityInfo = fileString[0: profileIndex].strip()
                #temp = activityInfo

                completeIndex = fileString.index(KEY_FRAME_COMPLETE) + len(KEY_FRAME_COMPLETE)
                secondProfileIndex = fileString.index(KEY, profileIndex + len(KEY))

                # 没有fps数据的不写入文件
                if completeIndex + 1 != secondProfileIndex:
                    temp = fileString[completeIndex: secondProfileIndex]
                    self.__fileStringMap[activityInfo] = self.__fileStringMap[activityInfo] + temp
                    # list.append(temp)

                # 截取 继续循环
                fileString = fileString[secondProfileIndex + len(KEY):]
                indexComplete = fileString.find(KEY_FRAME_COMPLETE)
                # print(temp)

        finally:
            file_object.close()

    def outputFile(self):
        # 遍历字典列表
        i = 1
        for key, values in self.__fileStringMap.items():
            file_output = open(
                "monitor_result_%s_%s" % (time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())), i), 'w')
            file_output.write(values)
            file_output.close()
            i = i + 1
