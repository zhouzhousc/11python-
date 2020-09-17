#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/16


def move_max(lst, max_index):
    """
    将索引0到max_index这个范围内的最大值移动到max_index位置上
    :param lst:
    :param max_index:
    :return:
    """
    for i in range(max_index):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]


def pop_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        print(i)
        move_max(lst, i)


# 答案认为是range(len(lst)-1, 1, -1)，个人觉得是range(len(lst)-1, 0, -1)，否则前两个排序不一定正确
if __name__ == '__main__':
    lst = [7, 6, 4, 2, 3, 1]
    pop_sort(lst)
    print(lst)
