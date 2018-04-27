#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("AndroidManifest.xml")
collection = DOMTree.documentElement

activities = collection.getElementsByTagName("activity")

i = 0
for activity in activities:
    i = i + 1
    print "*****第%s个Activity*****" % i
    if activity.hasAttribute("android:label"):
        print "android:label: %s" % activity.getAttribute("android:label")
    if activity.hasAttribute("android:name"):
        print "android:label: %s" % activity.getAttribute("android:name")

    # type = movie.getElementsByTagName('type')[0]
    # print "Type: %s" % type.childNodes[0].data
    # format = movie.getElementsByTagName('format')[0]
    # print "Format: %s" % format.childNodes[0].data
    # rating = movie.getElementsByTagName('rating')[0]
    # print "Rating: %s" % rating.childNodes[0].data
    # description = movie.getElementsByTagName('description')[0]
    # print "Description: %s" % description.childNodes[0].data
