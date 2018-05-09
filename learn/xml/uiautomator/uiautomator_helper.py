#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom
import commands
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class UiautomatorHelper:
    def __init__(self, _out_file_name):
        self.__out_file_name = _out_file_name
        self.__swipe_mode = "vertical"
        self.__bounds = ""

    def dump_parse(self):
        print "正在uiautomator dump "
        s, o = commands.getstatusoutput(
            "adb shell uiautomator dump /sdcard/ui.xml && adb pull /sdcard/ui.xml %s" % self.__out_file_name)
        if s == 0:
            print "dump成功 正在分析"
            self.parse()
        else:
            print "dump失败"

    def parse(self):
        DOMTree = xml.dom.minidom.parse(self.__out_file_name)
        collection = DOMTree.documentElement
        nodes = collection.getElementsByTagName("node")
        for node in nodes:
            if node.hasAttribute("class"):
                node_cls = node.getAttribute("class")
                if (node_cls == "android.support.v4.view.ViewPager") or (node_cls.count("ViewPager") > 0):
                    print "找到了%s,修改滑动模式为 混合滑动" % (node_cls)
                    self.__swipe_mode = "mix"
                    if node.hasAttribute("bounds"):
                        self.__bounds = node.getAttribute("bounds")
                        print "bounds:%s" % self.__bounds
                    return

    def swipe_mode(self):
        return self.__swipe_mode

    def bounds(self):
        return self.__bounds


if __name__ == "__main__":
    parser = UiautomatorHelper("temp.xml")
    parser.dump_parse()
    print parser.swipe_mode()
    print parser.bounds()
