#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def my_capitalize(string):
    if not string:
        return string

    lst = []
    for index, item in enumerate(string):
        ascii_index = ord(item)
        if index == 0:
            if 97 <= ascii_index <= 122:
                item = chr(ascii_index - 32)
        else:
            if 65 <= ascii_index <= 90:
                item = chr(ascii_index + 32)
        lst.append(item)

    return "".join(lst)


print(my_capitalize('this is A book'))
