#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


def my_sum(lst):
    """
    返回列表里所有数据的总和
    如果列表里有非数字类型的数据，忽略不管
    :param lst:
    :return: digit
    """
    sum_res = 0
    if not isinstance(lst, list):
        return sum_res

    for item in lst:
        if isinstance(item, (float, int)):
            sum_res += item

    return sum_res
