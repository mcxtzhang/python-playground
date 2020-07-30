#!/usr/bin/python
# -*- coding: UTF-8 -*-




def trim(img):
    img2 = img.sum(axis=2)
    (row, col) = img2.shape
    tempr0 = 0
    tempr1 = 0
    tempc0 = 0
    tempc1 = 0
    # 765 是255+255+255,如果是黑色背景就是0+0+0，彩色的背景，将765替换成其他颜色的RGB之和，这个会有一点问题，因为三个和相同但颜色不一定同
    for r in range(0, row):
        if img2.sum(axis=1)[r] != 765 * col:
            tempr0 = r
            break

    for r in range(row - 1, 0, -1):
        if img2.sum(axis=1)[r] != 765 * col:
            tempr1 = r
            break

    for c in range(0, col):
        if img2.sum(axis=0)[c] != 765 * row:
            tempc0 = c
            break

    for c in range(row - 1, 0, -1):
        if img2.sum(axis=0)[c] != 765 * row:
            tempc1 = c
            break

    new_img = img[tempr0:tempr1 + 1, tempc0:tempc1 + 1, 0:3]
    return new_img


