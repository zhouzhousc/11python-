#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


from collections.abc import Iterable


def my_len(obj):
    """
    获得obj对象的长度
    :param obj:
    :return:
    """
    if not isinstance(obj, Iterable):
        return None

    length = 0
    for item in obj:
        length += 1

    return length


# 注意判断是否可迭代对象的用法 ==>  isinstance(obj, Iterable)
if __name__ == '__main__':
    print(my_len('232'))
    print(my_len([3, 4, 2, 1]))
    print(my_len({'a': 4, 'b': 4}))
    print(my_len((3, 5, 6, 6, 3)))
    print(my_len(set([3, 5, 6, 6, 3])))
