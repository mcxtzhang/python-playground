#!/usr/bin/python
# -*- coding: UTF-8 -*-


class BTCError:
    def __init__(self, image_path, top, bottom, left, right):
        self.image_path = image_path
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right

    def printMsg(self):
        print "图片:%s,top：%s, bottom：%s, left:%s, right:%s ,有优化空间" % (
        self.image_path, self.top, self.bottom, self.left, self.right)
