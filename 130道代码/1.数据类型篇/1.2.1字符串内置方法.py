#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


# 1.将字符串 "abcd" 转成大写
# 2.计算字符串 "cd" 在 字符串 "abcd"中出现的位置
# 3.字符串 "a,b,c,d" ，请用逗号分割字符串，分割后的结果是什么类型的？
# 4."{name}喜欢{fruit}".format(name="李雷") 执行会出错，请修改代码让其正确执行
# 5.string = "Python is good", 请将字符串里的Python替换成 python,并输出替换后的结果
# 6.有一个字符串 string = "python修炼第一期.html"，请写程序从这个字符串里获得.html前面的部分，要用尽可能多的方式来做这个事情
# 7.如何获取字符串的长度？
# 8."this is a book",请将字符串里的book替换成apple
# 9."this is a book", 请用程序判断该字符串是否以this开头
# 10."this is a book", 请用程序判断该字符串是否以apple结尾
# 11."This IS a book"， 请将字符串里的大写字符转成小写字符
# 12."This IS a book"， 请将字符串里的小写字符，转成大写字符
# 13."this is a book\n"， 字符串的末尾有一个回车符，请将其删除

print("abcd".upper())
print("abcd".find("cd"))
print("a,b,c,d".split(","))
print("{name}喜欢{fruit}".format(name="李雷", fruit="pitch"))
print("Python is good".replace("Python", "python"))
string = "python修炼第一期.html"
print(string[:-5])
print(string[-6::-1])
print(len("python修炼第一期.html"))
print("this is a book".replace("book", "apple"))
print("this is a book".startswith("this"))
print("this is a book".endswith("apple"))
print("This IS a book".lower())
print("This IS a book".upper())
print("this is a book\n".strip())

print("ab is abb".split())
# None (the default value) means split according to any whitespace
# 默认是以任何空白字符切割


# 字符串切片那题做错了,切片操作记住两点，1是包左不包右，2是第三位代表起始方向和间隔，如-1
# 第6题：string[0:string.find('.html')] 或者string[0:-5]
