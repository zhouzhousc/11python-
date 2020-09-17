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
    将字符串string转成int类型数据
    不考虑string的类型,默认就是符合要求的字符串
    传入字符串"432" 返回整数432
    :param string:
    :return:
    """
    res = 0
    for item in string:
        int_value = str_int_dic[item]
        res = res * 10 + int_value

    return res


def my_float(string):
    """
    将字符串string转换成float类型数据
    :param string:
    :return:
    """
    arrs = string.split('.')
    int_value = my_int(arrs[0])
    float_value = my_int(arrs[1])
    while float_value > 1:
        float_value *= 0.1

    return int_value + float_value


if __name__ == '__main__':
    print(my_float("34.22"))
