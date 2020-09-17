#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


lst1 = [1, 2, 3, 5, 6, 3, 2]
lst2 = [2, 5, 7, 9]

# 1.哪些整数既在lst1中，也在lst2中
# 2.哪些整数在lst1中，不在lst2中
# 3.两个列表一共有哪些整数

# 像这种求交集，并集，差集的问题考虑变成 元组 再做

set1 = set(lst1)
set2 = set(lst2)

print(set1.intersection(set2))  # 交集
print(set1.difference(set2))    # 差集
print(set1.union(set2))         # 并集
