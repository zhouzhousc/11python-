#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


def my_max(seq):
    """
    返回序列里的最大值
    :param lst:
    :return:
    """
    max_value = None
    if not isinstance(seq, (list, tuple)):
        return max_value

    if len(seq) == 0:
        return max_value

    max_value = seq[0]
    for item in seq:
        if not isinstance(item, (float, int)):
            continue
        if item > max_value:
            max_value = item

    return max_value


def my_min(seq):
    """
    返回序列里的最小值
    :param lst:
    :return:
    """
    min_value = None
    if not isinstance(seq, (list, tuple)):
        return min_value

    if len(seq) == 0:
        return min_value

    min_value = seq[0]
    for item in seq:
        if not isinstance(item, (float, int)):
            continue

        if item < min_value:
            min_value = item

    return min_value
