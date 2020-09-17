#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def my_replace(source, oldsub, newsub):
    """
    将字符串里所有的oldsub子串替换成newsub
    :param source:
    :param oldsub:
    :param newsub:
    :return:
    """
    if not source or not oldsub:
        return source

    new_string = ""
    start_index = 0
    index = my_find(source, oldsub, start=start_index)
    while index != -1:
        new_string += source[start_index:index] + newsub
        start_index = index + len(oldsub)
        index = my_find(source, oldsub, start=start_index)

    new_string += source[start_index:]
    return new_string


def my_find(source, target, start=0):
    """
    返回字符串source中 子串target开始的位置， 从start索引开始搜索
    如果可以找到多个，返回第一个
    :param source:
    :param target:
    :param start:
    :return:
    """
    if not source or not target:
        return -1

    # 不合理的搜索起始位置
    if start < 0 or start >= len(source):
        return -1

    if len(target) > len(source):
        return -1

    for index in range(start, len(source) - len(target) + 1):
        t_index = 0
        while t_index < len(target):
            if target[t_index] == source[t_index + index]:
                t_index += 1
            else:
                break

        if t_index == len(target):
            return index

    return -1


# 是所有的旧子串都变成新子串，所有的
if __name__ == '__main__':
    print(my_replace('this is a book', 'this', 'it'))
    print(my_replace('this is a this book', 'this', 'it'))
    print(my_replace('this is a this bookthis', 't2his', 'it'))
