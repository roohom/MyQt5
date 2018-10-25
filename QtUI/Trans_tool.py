#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Trans_tool.py
# Author: roohom
# Date  : 2018/10/25 0025


import os
import os.path

dir = "./"


# 列出目录下所有的UI文件
def listUIFile():
    list = []
    files = os.listdir(dir)
    for each_file in files:
        if os.path.splitext(each_file)[1] == ".ui":
            list.append(each_file)

    return list


# 把扩展名为.ui的文件改程扩展名为.py的文件
def transPyFile(each_file):
    return os.path.splitext(each_file)[0] + ".py"


# 调用系统命令把UI文件转换为.py文件
def runMain():
    list = listUIFile()
    for uiFile in list:
        pyFile = transPyFile(uiFile)
        cmd = "pyuic5 -o {pyFile} {uiFile}".format(pyFile=pyFile, uiFile=uiFile)
        os.system(cmd)


if __name__ == '__main__':
    runMain()