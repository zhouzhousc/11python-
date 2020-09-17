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
            if target[t_index] == source[index + t_index]:
                t_index += 1
            else:
                break
        if len(target) == t_index:
            return index
    return -1


if __name__ == '__main__':
    print(my_find('this is a book', 'this'))
    print(my_find('this is a book', 'this', start=1))
    print(my_find('this is a book', 'book'))
    print(my_find('this is a book', 'k', start=10))
    print(my_find('this is a book', 'book', start=10))
    print(my_find('this is a book', 'a', start=3))
