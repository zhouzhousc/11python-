#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def is_startswith(source, substr):
    """
    判断字符串source是否以substr开头
    :param source:
    :param substr:
    :return:
    """
    if not source or not substr:
        return False

    if len(substr) > len(source):
        return False

    for index, item in enumerate(substr):
        if item != source[index]:
            break
    else:
        return True  # 如果for循环不是因为break结束的，就会进入到else语句块

    return False


if __name__ == '__main__':
    print(is_startswith("python", 'py'))
