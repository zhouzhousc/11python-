#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


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


def my_split(source, sep, maxsplit=-1):
    """
    以sep分割字符串source
    :param source:
    :param sep:
    :param maxsplit:
    :return:
    """
    if not source or not sep:
        return []

    lst = []
    max_split_count = maxsplit if maxsplit > 0 else len(source)
    split_count = 0

    start_index = 0
    index = my_find(source, sep, start=start_index)
    while split_count < max_split_count and index != -1:
        sep_str = source[start_index:index]
        lst.append(sep_str)
        split_count += 1
        start_index = index + len(sep)
        index = my_find(source, sep, start=start_index)

    sep_str = source[start_index:]
    lst.append(sep_str)

    return lst


if __name__ == '__main__':
    print(my_split("1,3,4", ','))
    print(my_split("1,,3,,4", ',,'))
    print(my_split("abcadae", 'a'))
    print(my_split("abcadae", 'a', maxsplit=2))
    print(my_split("aaaa", 'a'))
