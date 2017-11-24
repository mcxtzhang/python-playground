#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os


class ZUtils:
    '工具类'

    @staticmethod
    def getTimeSuffix():
        return "%s" % (time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())))

