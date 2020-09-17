#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


# 使用input函数接收用户的输入，如果用户输入的整数是偶数，则
# 使用print函数输出"你输入的整数是:{value}, 它是偶数",
# 如果是奇数，则使用print函数输出"你输入的整数是:{value}, 它是奇数"

i_value = int(input("请输出一个整数:"))
if i_value % 2 == 0:
    print("你输入的整数是：{value}, 它是偶数".format(value=i_value))
else:
    print("你输入的整数是：{value}, 它是奇数".format(value=i_value))

# 使用input函数接收用户的输入，如果输入的数据不可以转换成int类型数据，
# 则输出"无法使用int函数转换"，如果可以，则将用户的输入转成int类型数据并继续判断。

# 如果输入数据是奇数，则将其乘以2并输出，
# 如果是偶数，则判断是否能被4整除，如果可以则输出被4除后的值，
# 若不能被4整数，则判断是否大于20，如果大于20则输出与20的差值，如果小于等于20，则直接输出该值

value = input("请输入一个整数:")
if not value.isdigit():
    print('无法使用int函数转换')
else:
    i_value = int(value)
    if i_value % 2 == 1:
        print(i_value * 2)
    elif i_value % 4 == 0:
        print(i_value / 4)
    elif i_value > 20:
        print(i_value - 20)
    else:
        print(i_value)

# ======>>  注意 str.isdigit() 函数用法，判断一个字符串是否是 数字字符串
