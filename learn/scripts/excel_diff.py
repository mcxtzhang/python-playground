#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding=utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

###########################
# 对比两个版本的Excel数据的异同
###########################
import xlrd
import xlwt
import os
import os

print os.getcwd()  # 打印出当前工作路径
os.chdir(os.getcwd())  # 修改当前工作目录

l_p = []  # 定义两个全局list，分别存储原始和目的需要对比的数据
l_t = []


def read_excel():
    wb_pri = xlrd.open_workbook('/Users/zhangxutong/py/python-playground/learn/scripts/20200628_2.xlsx')  # 打开原始文件
    wb_tar = xlrd.open_workbook('./20200629.xlsx')  # 打开目标文件
    wb_result = xlwt.Workbook()  # 新建一个文件，用来保存结果
    sheet_result = wb_result.add_sheet('result', cell_overwrite_ok=True)
    result_i = 0
    result_j = 0
    for sheet_i in range(1):
        sheet_pri = wb_pri.sheet_by_index(sheet_i)  # 通过index获取每个sheet，为了省心，我根据自己的需要限定为第2-21个sheet
        sheet_tar = wb_tar.sheet_by_index(sheet_i)

        print(sheet_pri.name, sheet_tar.name)
        # 为什么是取这一列，因为这就是需要对比的数据阿
        l_p = sheet_pri.col_values(1)
        l_t = sheet_tar.col_values(1)
        print "sssss:%s" % l_p
        print "s222:%s" % l_t

        # tmp =[var for val in a if val in b] #这个是求交集,老大没要求是用不上的
        # 求参数在pri（原始数据）中存在，而在tar（目标）中不存在的
        tmp_pd = list(set(l_p).difference(set(l_t)))
        # 求参数在tar中存在，而在pri中不存在的
        tmp_td = list(set(l_t).difference(set(l_p)))

        print "tmp_pd:%s" % tmp_pd
        print "tmp_td:%s" % tmp_td

        if result_i < result_j:
            result_i = result_j
        else:
            result_j = result_i
        # for pd_i in tmp_pd:
        #     result_i = result_i + 1
        #     sheet_result.write(result_i, 0, sheet_pri.name)
        #     sheet_result.write(result_i, 2, pd_i)
        for td_i in tmp_td:
            result_j = result_j + 1
            sheet_result.write(result_j, 1, sheet_tar.name)
            sheet_result.write(result_j, 3, td_i)
    # 好了，可以去名为result的excel中查看结果了
    wb_result.save('result.xls')


if __name__ == '__main__':
    read_excel()
