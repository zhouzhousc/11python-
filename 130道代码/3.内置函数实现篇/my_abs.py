#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


def my_abs(number):
    if isinstance(number, (int, float)):
        if number >= 0:
            return number
        else:
            return -number
    else:
        raise TypeError("bad operand type for my_abs(): 'str'")


print(my_abs("9"))

#  注意第13行的 自定义错误 的用法

