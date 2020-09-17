#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/17


lst = [4, 1, 67, 34, 12, 35, 14, 8, 6, 19]
length = len(lst)
step = length // 2

while step > 0:

    for i in range(step):
        # 插入排序
        for j in range(i + step, length, step):
            if lst[j] < lst[j - step]:
                tmp = lst[j]
                k = j - step

                while k >= 0 and lst[k] > tmp:
                    lst[k + step] = lst[k]
                    k -= step

                lst[k + step] = tmp
    step //= 2  # 缩小增量

print(lst)
