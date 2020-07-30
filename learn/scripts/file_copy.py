#!/usr/bin/python
# -*- coding: UTF-8 -*-

from shutil import copyfile
from sys import exit

# source = input("Enter source file with full path: ")
# target = input("Enter target file with full path: ")


source = "/Users/zhangxutong/Desktop/mem-dump/temp/pic_1.png"
source = "/Users/zhangxutong/Desktop/mem-dump/temp/activity_main.xml"

# adding exception handling

for i in range(0, 1000):
    try:
        target = "/Users/zhangxutong/Desktop/mem-dump/temp/pic_copy2_%s.png" % i
        target = "/Users/zhangxutong/Desktop/mem-dump/temp/activity_main_%s.xml" % i
        copyfile(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
        exit(1)
    except:
        print("Unexpected error:", exit.exc_info())
        exit(1)


# print("\nFile copy done!\n")
#
# while True:
#     print("Do you like to print the file ? (y/n): ")
#     check = input()
#     if check == 'n':
#         break
#     elif check == 'y':
#         file = open(target, "r")
#         print("\nHere follows the file content:\n")
#         print(file.read())
#         file.close()
#         print()
#         break
#     else:
#         continue
