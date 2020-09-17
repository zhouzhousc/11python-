#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


lst = [1, [4, 6], True]


# 请将列表里所有数字修改成原来的两倍
# 注意 enumerate()用法、isinstance()用法、递归用法

def double_list(list0):
    for index, item in enumerate(list0):
        if isinstance(item, bool):
            continue
        if isinstance(item, list):
            double_list(item)
        if isinstance(item, (int, float)):
            list0[index] = item * 2

    return list0


print(double_list(lst))
