#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


dic = {
    'python': 95,
    'java': 99,
    'c': 100
}

# 1.字典的长度是多少
# 2.请修改'java' 这个key对应的value值为98
# 3.删除 c 这个key    ======>>     重点看看
# 4.增加一个key-value对，key值为 php, value是90
# 5.获取所有的key值，存储在列表里
# 6.获取所有的value值，存储在列表里
# 7.判断 javascript 是否在字典中
# 8.获得字典里所有value 的和
# 9.获取字典里最大的value
# 10.获取字典里最小的value
# 11.字典 dic1 = {'php': 97}， 将dic1的数据更新到dic中

print(len(dic))
dic["java"] = 98
del dic["c"]
dic["php"] = 90
print(dic)
list_key = [item for item in dic.keys()]
# list_key = list(dic.keys())
print(list_key)
list_value = [item for item in dic.values()]
# list_value = list(dic.values())
print(list_value)
print("javascript" in dic.keys())
print(sum(dic.values()))
print(max(dic.values()))
print(min(dic.values()))
dic1 = {'php': 97}
dic.update(dic1)
print(dic)
