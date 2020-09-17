#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


dic = {
    'python': 90,
    'java': 95
}

for key in dic:
    print(key, dic[key])

for key, value in dic.items():
    print(key, value)

for key in dic.keys():
    print(key)

for value in dic.values():
    print(value)

# 注意区别 dic, dic.items()，dic.keys()，dic.values()
