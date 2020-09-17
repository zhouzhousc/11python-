#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def islower(string):
    """
    如果字符串string 里所有区分大小写的字符都是小写，则返回True
    :param string:
    :return:
    """
    if not string:
        return False

    for item in string:
        if 65 <= ord(item) <= 90:
            return False

    return True


if __name__ == '__main__':
    print(islower('232r'))
