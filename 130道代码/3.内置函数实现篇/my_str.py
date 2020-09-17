#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


int_str_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}


def my_str(int_value):
    """
    将整型转换成字符串
    简单的实现int转str即可，原str函数功能非常强大
    :param int_value:
    :return: str
    """
    if int_value == 0:
        return '0'

    lst = []
    is_positive = True
    if int_value < 0:
        is_positive = False
        int_value = abs(int_value)

    while int_value:
        number = int_value % 10
        int_value //= 10
        str_number = chr(number + 48)
        lst.append(str_number)

    if not is_positive:
        lst.append('-')

    lst = lst[::-1]
    return ''.join(lst)


# 重点看看过程，以及join()的用法
if __name__ == '__main__':
    print(my_str(0))
    print(my_str(123))
    print(my_str(-123))
