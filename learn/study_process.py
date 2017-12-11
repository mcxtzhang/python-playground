#!/usr/bin/python
# -*- coding: UTF-8 -*-
from multiprocessing import Process
import os


# 子进程要执行的代码
import time


def run_proc(params):
    while 1:
        print "I am subprocess %s,with %s" % (os.getpid(), params)
        time.sleep(0.1)


if __name__ == '__main__':
    print "I am mainprocess:%s" % os.getpid()
    p = Process(target=run_proc, args=('param1',))

    p.start()

    print "I am still mainprocess:%s" % os.getpid()

    time.sleep(1)
    p.terminate()
