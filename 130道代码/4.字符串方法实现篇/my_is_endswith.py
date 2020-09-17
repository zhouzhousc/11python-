#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/15


def is_endswith(source, substr):
    """
    判断字符串source 是否以substr结尾
    :param source:
    :param substr:
    :return:
    """
    if not source or not substr:
        return False

    if len(substr) > len(source):
        return False

    start_index = len(source) - len(substr)
    for index in range(start_index, len(source)):
        if source[index] != substr[index - start_index]:
            break
    else:
        return True

    return False


if __name__ == '__main__':
    print(is_endswith("python", 'thon'))
