#!/usr/bin/python
# -*- coding: UTF-8 -*-
import platform

import os


def getSeparator():
    if 'Windows' in platform.system():
        separator = '\\'
    else:
        separator = '/'
    return separator


def findPath(file):
    o_path = os.getcwd()
    separator = getSeparator()
    str = o_path
    str = str.split(separator)
    while len(str) > 0:
        spath = separator.join(str) + separator + file
        leng = len(str)
        if os.path.exists(spath):
            return spath
        str.remove(str[leng - 1])
