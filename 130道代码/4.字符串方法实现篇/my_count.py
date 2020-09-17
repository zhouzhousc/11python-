#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def my_count(source, target, start, end):
    """
    函数返回字符串source在start 和 end之前，子串target 的数量， 索引范围左闭右开
    :param source:
    :param target:
    :param start:
    :param end:
    :return:
    """
    if not source or not target:
        return 0

    if start >= end:
        return 0

    if start < 0 or start >= len(source):
        return 0

    if end > len(source):
        end = len(source)

    count = 0
    index = start

    while index < end:
        t_index = 0
        while t_index < len(target) and index + len(target) <= end:
            if target[t_index] != source[index + t_index]:
                break
            t_index += 1

        if t_index == len(target):
            index += len(target)
            count += 1
        else:
            index += 1

    return count


source = "this is a book"
target = 'is'

print(my_count(source, target, 0, len(source)))
