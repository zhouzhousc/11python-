#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def my_enumerate(lst):
    """
    实现和enumerate 类似的功能
    :param lst:
    :return:
    """
    for i in range(len(lst)):
        yield i, lst[i]


lst = ['a', 'b', 'c']
for index, item in my_enumerate(lst):
    print(index, item)
