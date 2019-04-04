#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List, Tuple
import timeit


def two_sum_brute_force(array: List, target: int):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    >>> two_sum_brute_force(array=[2, 7, 11, 15], target=9)
    (0, 1)

    暴力搜索: O(N^2)
    """
    for i, u in enumerate(array):
        for j, v in enumerate(array[i + 1:]):
            if u + v == target:
                return i, j + i + 1
    return None


def two_sum_using_sort(array: List, target: int):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    >>> two_sum_using_sort(array=[2, 7, 11, 15], target=9)
    (0, 1)

    利用排序: O(NlogN)
    """
    origin_index = sorted(range(len(array)), key=lambda k: array[k])
    sorted_array = [array[i] for i in origin_index]

    i = 0
    j = len(array) - 1
    while i < j:
        sum_ij = sorted_array[i] + sorted_array[j]
        if sum_ij == target:
            return origin_index[i], origin_index[j]

        if sum_ij < target:
            i = i + 1
        else:
            j = j - 1
    return None


def two_sum(array: List, target: int) -> Tuple[int, int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    >>> two_sum(array=[2, 7, 11, 15], target=9)
    (0, 1)

    利用HashMap: 一次遍历，输出结果, O(N)
    """
    hash_map = {}
    for i, v in enumerate(array):
        complement = target - v
        if complement in hash_map:
            return hash_map[complement], i

        hash_map[v] = i
    return None


def analysis():

    def wraped(f, *args, **kwargs):
        def wrap():
            return f(*args, **kwargs)
        return wrap

    import numpy as np
    array = list(np.random.randint(0, 100, 100))
    target = 128
    t_brute_force = timeit.timeit(wraped(two_sum_brute_force, array, target))
    t_using_sort = timeit.timeit(wraped(two_sum_using_sort, array, target))
    t = timeit.timeit(wraped(two_sum, array, target))

    print("t(brute_force)={}\nt(using_sort)={}\nt={}".format(t_brute_force, t_using_sort, t))


if __name__ == '__main__':
    analysis()
