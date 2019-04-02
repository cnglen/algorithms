"""
Implement Flatten Arrays.

Given an array that may contain nested arrays, produce a single resultant array.


总结:
- 递归调用
- collections.abc.Iterable: Checking isinstance(obj, Iterable) detects classes that are registered as Iterable or that have an __iter__() method

"""
from collections import Iterable
from typing import List


def flatten(input_arr, output_arr=None) -> List:
    """
    return list
    """
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)  # tail-recursion
        else:
            output_arr.append(ele)  # produce the result
    return output_arr


def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten_iter(element)
        else:
            yield element
