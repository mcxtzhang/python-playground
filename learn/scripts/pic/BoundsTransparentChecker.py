#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

from PIL import Image
from PIL import ImageFilter

from learn.scripts.pic.BTCError import BTCError

DEBUG = False


class BoundsTransparentChecker:
    def __init__(self, image_path, bounds_check_threshold=None):
        self.__image_path = image_path
        if bounds_check_threshold == None:
            bounds_check_threshold = 3
        self.__bounds_check_threshold = bounds_check_threshold
        pass

    def boot(self):
        image = Image.open(self.__image_path)
        image.convert("RGBA")
        result_top = self.checkBoundsTransparentTop(image)
        result_bottom = self.checkBoundsTransparentBottom(image)
        result_left = self.checkBoundsTransparentLeft(image)
        result_right = self.checkBoundsTransparentRight(image)
        if result_top or result_bottom or result_left or result_right:
            return BTCError(self.__image_path, result_top, result_bottom, result_left, result_right)
        else:
            return None

    def checkBoundsTransparentTop(self, image):
        pixdatas = image.load()
        bounds_check_threshold = min(self.__bounds_check_threshold, image.size[1])
        # 自上而下，逐行扫描
        for y in xrange(bounds_check_threshold):
            for x in xrange(image.size[0]):
                pixel = pixdatas[x, y]
                if DEBUG:
                    print "x:%s, y:%s, pixel:%s" % (x, y, pixel)
                if pixel[3] != 0:
                    print "自上而下有 x:%s, y:%s 不是透明的，跳出检测" % (x, y)
                    return False

        print "这张图片自上而下，前%s行都是透明的，有优化空间." % self.__bounds_check_threshold
        return True

    def checkBoundsTransparentBottom(self, image):
        pixdatas = image.load()
        bounds_check_threshold = min(self.__bounds_check_threshold, image.size[1])
        # 自下而上，逐行扫描
        for y in xrange(image.size[1] - bounds_check_threshold, image.size[1]):
            for x in xrange(image.size[0]):
                pixel = pixdatas[x, y]
                if DEBUG:
                    print "x:%s, y:%s, pixel:%s" % (x, y, pixel)
                if pixel[3] != 0:
                    print "自下而上有 x:%s, y:%s 不是透明的，跳出检测" % (x, y)
                    return False

        print "这张图片自下而上，最后%s行都是透明的，有优化空间." % self.__bounds_check_threshold
        return True

    def checkBoundsTransparentLeft(self, image):
        pixdatas = image.load()
        bounds_check_threshold = min(self.__bounds_check_threshold, image.size[0])
        # 自左而右，逐列扫描
        for x in xrange(bounds_check_threshold):
            for y in xrange(image.size[1]):
                pixel = pixdatas[x, y]
                if DEBUG:
                    print "x:%s, y:%s, pixel:%s" % (x, y, pixel)
                if pixel[3] != 0:
                    print "从左向右有 x:%s, y:%s 不是透明的，跳出检测" % (x, y)
                    return False

        print "这张图片从左向右，前%s列都是透明的，有优化空间." % self.__bounds_check_threshold
        return True

    def checkBoundsTransparentRight(self, image):
        pixdatas = image.load()
        bounds_check_threshold = min(self.__bounds_check_threshold, image.size[0])
        # 自左而右，逐列扫描
        for x in xrange(image.size[0] - bounds_check_threshold, image.size[0]):
            for y in xrange(image.size[1]):
                pixel = pixdatas[x, y]
                if DEBUG:
                    print "x:%s, y:%s, pixel:%s" % (x, y, pixel)
                if pixel[3] != 0:
                    print "从右向左有 x:%s, y:%s 不是透明的，跳出检测" % (x, y)
                    return False

        print "这张图片从右向左，最后%s列都是透明的，有优化空间." % self.__bounds_check_threshold
        return True


if __name__ == '__main__':
    checker = BoundsTransparentChecker("./cropped.png")
    checker = BoundsTransparentChecker("./alpha_pic_1.png")
    result = checker.boot()
    if result:
        result.printMsg()
    else:
        print "这张图片没毛病"
