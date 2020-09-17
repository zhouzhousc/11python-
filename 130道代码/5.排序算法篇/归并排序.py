#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/9/17


def merge_lst(left_lst, right_lst):
    """
    合并有序序列函数实现
    合并的方法就是分别从两个已经 有序 ， 有序 序列中拿出一个数来进行比较，小的那一个放到新序列中，
    然后，从这个小的数所属的序列中拿出一个数来继续比较
    :param left_lst:
    :param right_lst:
    :return:
    """
    left_index, right_index = 0, 0
    res_lst = []
    while left_index < len(left_lst) and right_index < len(right_lst):
        # 小的放入到res_lst中
        if left_lst[left_index] < right_lst[right_index]:
            res_lst.append(left_lst[left_index])
            left_index += 1
        else:
            res_lst.append(right_lst[right_index])
            right_index += 1

    # 循环结束时,必然有一个序列已经都放到新序列里,另一个却没有
    if left_index == len(left_lst):
        res_lst.extend(right_lst[right_index:])
    else:
        res_lst.extend(left_lst[left_index:])

    return res_lst


def merge_sort(lst):
    """
    一层一层的分组，分到最后，一个组里只有一个元素，
    终于符合合并有序序列的条件了，再一层一层的向上合并
    :param lst:
    :return:
    """
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left_lst = merge_sort(lst[:middle])
    right_lst = merge_sort(lst[middle:])
    return merge_lst(left_lst, right_lst)


if __name__ == '__main__':
    lst = [19, 4, 2, 8, 3, 167, 174, 34]
    print(merge_sort(lst))
