#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

DIR_STUFFS = "stuffs"
DIR_PROCESSED_STUFFS = "processed_stuffs"


class stuff_file:
    '目录创建 删除 管理类'

    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        stuff_path = stuff_file.get_stuff_dir()
        if not os.path.exists(stuff_path):
            os.mkdir(stuff_path)

        processed_stuff_path = stuff_file.get_processed_stuff_dir()
        if not os.path.exists(processed_stuff_path):
            os.mkdir(processed_stuff_path)

    @staticmethod
    def get_stuff_dir():
        cur_path = os.path.abspath('.')
        # print cur_path

        stuff_path = os.path.join(cur_path, DIR_STUFFS)
        # print stuff_path
        return stuff_path

    @staticmethod
    def get_processed_stuff_dir():
        cur_path = os.path.abspath('.')
        return os.path.join(cur_path, DIR_PROCESSED_STUFFS)

    @staticmethod
    def clean_dirs():
        directorys = [DIR_STUFFS, DIR_PROCESSED_STUFFS]
        for i, directory in enumerate(directorys):
            # print directory
            if os.path.isdir(directory):
                file_ist = os.listdir(directory)
                for fileName in file_ist:
                    try:
                        os.remove(os.path.join(directory,fileName))
                    except:
                        print "s.remove(%s+" / "+%s)  error!" % (directory, fileName)
            else:
                print "%s is not directory" % directory
