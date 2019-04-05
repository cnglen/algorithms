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
import timeit
import numpy as np


def three_sum_brute_force(array: List[int], target: int) -> Tuple[int, int, int]:
    """
    args:
      array:
      target:

    returns:
      idxs

    >>> s = [-1, 0, 1, 2, -1, -4]
    >>> three_sum_brute_force(s, 0)
    (0, 1, 2)

    O(N^3)
    """

    for i, u in enumerate(array):
        for j, v in enumerate(array):
            for k, w in enumerate(array):
                if j > i and k > j and u + v + w == target:
                    return i, j, k

    return None


def three_sum_using_sort(array: List[int], target: int) -> Tuple[int, int, int]:
    """
    args:
      array:
      target:

    returns:
      idxs

    >>> s = [-1, 0, 1, 2, -1, -4]
    >>> three_sum_hash_map(s, 0)
    (0, 1, 2)

    O(NlogN) + O(N^2) = O(N^2)
    """

    origin_index = list(np.argsort(array))
    sorted_array = [array[i] for i in origin_index]

    for i, u in enumerate(sorted_array[:-2]):
        j, k = i + 1, len(sorted_array) - 1
        while j < k:
            sum_jk = sorted_array[j] + sorted_array[k]
            if sum_jk + u == target:
                return origin_index[i], origin_index[j], origin_index[k]

            if sum_jk + u < target:
                j += 1
            else:
                k -= 1

    return None


from collections import defaultdict


def three_sum_hash_map(array: List[int], target: int) -> Tuple[int, int, int]:
    """
    args:
      array:
      target:

    returns:
      idxs

    >>> s = [-1, 0, 1, 2, -1, -4]
    >>> three_sum_hash_map(s, 0)
    (0, 1, 2)

    O(N^2) + O(N) = O(N^2)
    """
    hash_map_one = defaultdict(list)
    for k, w in enumerate(array):
        hash_map_one[w].append(k)

    for i, u in enumerate(array):
        for j, v in enumerate(array):
            if j > i:
                complement = target - u - v
                for k in hash_map_one[complement]:
                    if k not in [i, j]:
                        return i, j, k

    return None

    # res = set()
    # array.sort()                # O(NlgN)
    # for i in range(len(array) - 2):
    #     if i > 0 and array[i] == array[i - 1]:
    #         continue
    #     l, r = i + 1, len(array) - 1
    #     while l < r:
    #         s = array[i] + array[l] + array[r]
    #         if s > 0:
    #             r -= 1
    #         elif s < 0:
    #             l += 1
    #         else:
    #             # found three sum
    #             res.add((array[i], array[l], array[r]))

    #             # remove duplicates
    #             while l < r and array[l] == array[l + 1]:
    #                 l += 1

    #             while l < r and array[r] == array[r - 1]:
    #                 r -= 1

    #             l += 1
    #             r -= 1
    # return res


def analysis():
    """
    analysis of all implementations
    """
    def wraped(f, *args, **kwargs):
        """
        return a callable object for timeit.timeit
        """
        def wrap():
            return f(*args, **kwargs)
        return wrap

    N = 10000
    array = list(np.random.choice(N * 10, N, replace=False))
    target = 16384
    run_number = 10

    print(three_sum_brute_force(array, target))
    print(three_sum_using_sort(array, target))
    print(three_sum_hash_map(array, target))

    t_brute_force = timeit.timeit(wraped(three_sum_brute_force, array, target), number=run_number)
    t_using_sort = timeit.timeit(wraped(three_sum_using_sort, array, target), number=run_number)
    t = timeit.timeit(wraped(three_sum_hash_map, array, target), number=run_number)

    print("analysis of three_sum")
    print("t(brute_force)={:.3f}\nt(using_sort )={:.3f}\nt(using_hash )={:.3f}".format(t_brute_force, t_using_sort, t))


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    analysis()


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

        注意：答案中不可以包含重复的三元组。

        例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

        满足要求的三元组集合为：
        [
          [-1, 0, 1],
          [-1, -1, 2]
        ]
        >>> nums = [-1, 0, 1, 2, -1, -4]
        >>> Solution().threeSum(nums)

        """
        result = set()
        sorted_nums = sorted(nums)
        for i, u in enumerate(sorted_nums[:-2]):

            j, k = i + 1, len(sorted_nums) - 1
            while j < k:
                if u + sorted_nums[j] + sorted_nums[k] == 0:
                    result.add((u, sorted_nums[j], sorted_nums[k]))
                    j += 1
                    k -= 1
                elif u + sorted_nums[j] + sorted_nums[k] > 0:
                    k -= 1
                else:
                    j += 1
        return [list(e) for e in result]
