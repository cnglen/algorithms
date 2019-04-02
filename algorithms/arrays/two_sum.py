"""

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""

from typing import List, Tuple


def two_sum(array: list, target: int) -> Tuple[int, int]:
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i

        dic[target - num] = i
    return None


def two_sum(array: List, target: int) -> Tuple[int, int]:
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    >>> two_sum(array=[2, 7, 11, 15], target=9)
    (0, 1)

    一次遍历，输出结果, O(N)
    """
    hash_map = {}
    for i, v in enumerate(array):
        complement = target - v
        if complement in hash_map:
            return hash_map[complement], i

        hash_map[complement] = i
    return None


def two_sum(array, target):
    """
    an algorithm that, given a set S of n integers and another integer x,
    determines whether or not there exist two elements in S whose sum is exactly x.
    :param x:
    :param array:
    :return:
    """
    sorted_array = sorted(array)
    origin_index = sorted(range(len(array)), key=lambda k: array[k])
    i = 0
    j = len(array) - 1
    while i < j:
        sum = sorted_array[i] + sorted_array[j]
        if sum == target:
            return origin_index[i], origin_index[j]
        elif sum < target:
            i = i + 1
        else:
            j = j - 1
    return None
