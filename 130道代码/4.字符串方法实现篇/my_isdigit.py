#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def isdigit(string):
    """
    判断字符串只包含数字
    :param string:
    :return:
    """
    if not string:
        return False

    for item in string:
        if not (48 <= ord(item) <= 57):
            return False

    return True


if __name__ == '__main__':
    print(isdigit('232'))
    print(isdigit('232r'))
    print(isdigit(''))
