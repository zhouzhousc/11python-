#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def my_bin(value):
    """
    返回正整数value的二进制形式
    :param value:
    :return:
    """
    lst = []
    while value:
        if value % 2 == 1:
            lst.append('1')
        else:
            lst.append('0')

        value = value >> 1

    lst = lst[::-1]
    return ''.join(lst)


print(bin(10))

# 函数bin可以获得整数的二进制形式
if __name__ == '__main__':
    print(my_bin(3))
    print(my_bin(8))
    print(my_bin(10))

# 在算法面试中，有一道题目经常被使用，它要求应聘者计算一个整数的二进制中1的个数。
# 解决的思路是判断二进制最后一位是否为1，如果为1，则计数器加1，
# 判断完成后，整数向右位移一位（使用位运算符 >>） ，继续判断二进制的最后一位是否为1.
#
# 记住这种二进制位运算思路
