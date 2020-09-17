#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


lst = [1, 2, 3]
lst2 = [4, 5, 6]

print(id(lst))
lst += lst2
print(id(lst))
lst.extend(lst2)
print(id(lst))

# 过程中不会产生新的列表，id()方法查看内存地址,列表是可变对象

str1 = "1,2,3"
str2 = "4,5,6"
print(id(str1))
str1 += str2
print(id(str1))

# 过程中产生新的字符串并赋值给str1，字符串是不可变对象
# 合并前后str1的内存地址是不一样的
