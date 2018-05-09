#!/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("temp.xml")
collection = DOMTree.documentElement
# 在集合中获取所有电影
movies = collection.getElementsByTagName("node")

# 打印每部电影的详细信息
for movie in movies:
    print "*****Node*****"
    if movie.hasAttribute("index"):
        print "index: %s" % movie.getAttribute("index")
    if movie.hasAttribute("text"):
        print "text: %s" % movie.getAttribute("text")
    if movie.hasAttribute("class"):
        print "class: %s" % movie.getAttribute("class")
    if movie.hasAttribute("bounds"):
        print "bounds: %s" % movie.getAttribute("bounds")

class Translator:
    def __init__(self):
        pass
