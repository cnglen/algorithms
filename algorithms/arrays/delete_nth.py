"""
Given a list lst and a number N, create a new list that contains each number of the list at most N times without reordering.

For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3]

总结:
- 新的数据结构 collections.defaultdict, 是内置 dict 类的子类，第一个参数为default_factory，通过 default_factory 方法提供了一个初始值，比如default_factory=int, 使 defaultdict 在计数方面发挥好的作用, int()返回0
"""


import collections


def delete_nth_naive(array, n):
    """
    Time complexity O(n^2)
    """
    ans = []
    for num in array:
        if ans.count(num) < n:
            ans.append(num)
    return ans


def delete_nth(array, n):
    """
    Time Complexity O(n), using hash tables (hash map).
    """
    result = []
    counts = collections.defaultdict(int)  # keep track of occurrences

    for i in array:
        if counts[i] < n:
            result.append(i)
            counts[i] += 1

    return result
