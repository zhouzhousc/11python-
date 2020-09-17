#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


# 已知一个列表
# lst = [1,2,3,4,5]
#
# 1.求列表的长度
# 2.判断6 是否在列表中
# 3.lst + [6, 7, 8] 的结果是什么？
# 4.lst*2 的结果是什么
# 5.列表里元素的最大值是多少
# 6.列表里元素的最小值是多少
# 7.列表里所有元素的和是多少
# 8.在索引1的后面新增一个的元素10
# 9.在列表的末尾新增一个元素20

# 10.找出列表里最大值的个数
# 11.计算列表里元素的平均值
# 12.找出元素6在列表中的索引

lst = [1, 2, 3, 4, 5]
print(len(lst))
print(6 in lst)
print(lst + [6, 7, 8])
print(lst * 2)
print(max(lst))
print(min(lst))
print(sum(lst))
lst.insert(1, 10)
lst.append(20)
print(lst)

print(lst.count(max(lst)))
print(sum(lst) / float(len(lst)))
print(lst.index(1))
