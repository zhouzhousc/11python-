#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


str_int_dic = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def my_int(string):
    """
    将string类型转成int型
    不考虑字符串类型，默认就是符合要求的字符串
    :param string:
    :return: int
    """
    res = 0
    for item in string:
        int_value = str_int_dic[item]
        res = res * 10 + int_value
    return res


# 不会的重点看看
if __name__ == '__main__':
    print(my_int('432'))
    print(4 // 10)
