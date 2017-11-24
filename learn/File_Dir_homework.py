#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

cur_path = os.path.abspath('.')
print cur_path

stuff_path = os.path.join(cur_path, 'stuff')
print stuff_path

if not os.path.exists(stuff_path):
    os.mkdir(stuff_path)

processed_stuff_path = os.path.join(cur_path, "processed_stuffs")

if not os.path.exists(processed_stuff_path):
    os.mkdir(processed_stuff_path)

