#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def lower(string):
    """
    将字符串string里所有的大写字母改成小写字母，并返回一个新的字符串
    :param string:
    :return:
    """
    if not string:
        return None

    lst = list(string)
    for index, item in enumerate(lst):
        ascii_index = ord(item)
        if 65 <= ascii_index <= 90:
            s = chr(ascii_index + 32)
            lst[index] = s

    return ''.join(lst)


# 注意 ord() 方法的使用
# ord 函数获得这个字符的ASCII码表的十进制数值
if __name__ == '__main__':
    print(lower('232rSFD'))
