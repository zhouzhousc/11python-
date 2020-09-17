#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/14


# 1. 4.0 == 4       True
# 2. "4.0" == 4     False
# 3. bool("1")      True
# 4. bool("0")      True
# 5. str(32)        "32"
# 6. int(6.26)      6
# 7. float(32)      32.0
# 8. float("3.21")  3.21
# 9. int("434")     434
# 10. int("3.42")   3       ======>>   结果是报错了
# 11. bool(-1)      True
# 12. bool("")      False
# 13. bool(0)       False
# 14. "wrqq" > "acd"        True
# 15. "ttt" == "ttt "       False
# 16. "sd"*3                "sdsdsd"
# 17. "wer" + "2322"        "wer2322"

print(4.0 == 4)
print("4.0" == 4)
print("1")
print("0")
print(str(32))
print(int(6.26))
print(float(32))
print(float("3.21"))
print(int("434"))
# print(int("3.42"))    报错
print(bool(-1))
print(bool(""))
print(bool(0))
print("wrqq" > "acd")
print("ttt" == "ttt ")
print("sd"*3)
print("wer" + "2322")


# 结论
# 0 , 空字符串, None在条件判断语句中等价于False, 其他数值都等价于True
# bool函数在做数据类型转换时遵循该原则

# 两个字符串在比较大小时，比的不是长度，而是内容
# 字符串左对齐后，逐个字符依次比较，直到可以分出胜负

