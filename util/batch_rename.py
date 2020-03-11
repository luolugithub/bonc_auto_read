# -*- coding: utf-8 -*-
# @Time    : 12/12/19 10:22 AM
# @Author  : luolu
# @Email   : argluolu@gmail.com
# @File    : batch_rename.py
# @Software: PyCharm
import glob
import os

path = "/home/xkjs/PycharmProjects/pix2pixHD/datasets/bopian/dyzg_label"
dirs = os.listdir(path)


def rename():
    for item in dirs:
        # print(path + "/" + item)
        if os.path.isfile(path + "/" + item):
            # print(path + "/" + item)
            print(path + "/" + "dyzg_" + item)
            # print(item.split(" ")[-1].split("_")[1].replace(".", ""))
            # new_name = item.split(" ")[-1].split("_")[1].replace(".", "")
            os.rename(path + "/" + item,
                      path + "/" + "dyzg_" + item)



rename()