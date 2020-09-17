#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/16


def insert(lst, index):
    """
    列表lst从索引0到索引index-1 都是有序的
    函数将索引index位置上的元素插入到前面的一个合适的位置
    :param lst:
    :param index:
    :return:
    """
    if lst[index - 1] < lst[index]:
        return

    tmp = lst[index]
    tmp_index = index
    while tmp_index > 0 and lst[tmp_index - 1] > tmp:
        lst[tmp_index] = lst[tmp_index - 1]
        tmp_index -= 1
    lst[tmp_index] = tmp


def insert_sort(lst):
    for i in range(1, len(lst)):
        insert(lst, i)


if __name__ == '__main__':
    lst = [1, 6, 2, 2, 7, 5]
    insert_sort(lst)
    print(lst)
