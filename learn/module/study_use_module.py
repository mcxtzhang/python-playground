#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print "Hello 0 param"
    elif len(args) == 2:
        print "Hello 1 param:%s" % args[1]
    else:
        print "Many params:%s" % args


if __name__ == "__main__":
    test()
