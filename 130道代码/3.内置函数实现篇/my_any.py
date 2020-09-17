#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def my_any(lst):
    """
    列表lst中有一个True,则函数返回True
    :param lst:
    :return:
    """
    for item in lst:
        if item:
            return True

    return False


# any函数用于判断给定的可迭代参数 iterable 中的所有元素是否至少有一个为True
if __name__ == '__main__':
    print(my_any([True, False, False]))
