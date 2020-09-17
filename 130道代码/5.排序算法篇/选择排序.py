#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/17


def select_sort(lst):
    min = lst[0]
    for i in range(len(lst)):
        if i < min:
            lst[0] = lst[i]
