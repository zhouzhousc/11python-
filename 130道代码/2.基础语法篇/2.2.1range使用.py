#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14

lst = [i for i in range(3, 20, 4)]
print(lst)
lst = list(range(10, -3, -4))
print(lst)
lst = list(range(10, 5))  # ======>>  这种是空列表
print(lst)
lst = list(range(2, 12))
print(lst)

# 利用range函数遍历列表
lst = [1, 3, 5, 2, 7, 9]
for index in range(len(lst)):
    # 正序遍历
    print(lst[index])

    # 反向遍历
    print(lst[-(index + 1)])

    # 遍历偶数
    if lst[index] % 2 == 0:
        print(lst[index])

    # 遍历大于3的奇数
    if lst[index] % 2 == 1 and lst[index] > 3:
        print(lst[index])

