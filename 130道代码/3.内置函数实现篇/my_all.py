#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def my_all(seq):
    """
    如果列表里所有的元素都是True,则函数返回True,反之,返回False
    :param seq: 列表
    :return:
    """
    for item in seq:
        if not item:
            return False

    return True


# all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 True
if __name__ == '__main__':
    print(my_all([True, False, True]))
