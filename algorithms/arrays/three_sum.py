"""
Given an array S of n integers, are there three distinct elements a, b, c in S such that a + b + c = 0?

Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
"""

from typing import List, Tuple, Set


def three_sum(array: List[int]) -> Set[Tuple[int, int, int]]:
    """
    >>> s = [-1, 0, 1, 2, -1, -4]
    >>> three_sum(s)
    {(-1, -1, 2), (-1, 0, 1)}
    """
    res = set()
    array.sort()                # O(NlgN)
    for i in range(len(array) - 2):
        if i > 0 and array[i] == array[i - 1]:
            continue
        l, r = i + 1, len(array) - 1
        while l < r:
            s = array[i] + array[l] + array[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                # found three sum
                res.add((array[i], array[l], array[r]))

                # remove duplicates
                while l < r and array[l] == array[l + 1]:
                    l += 1

                while l < r and array[r] == array[r - 1]:
                    r -= 1

                l += 1
                r -= 1
    return res
