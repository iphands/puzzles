from ..common.utils import log, check, ListNode
import cProfile

import re


class Solution:
    def findPeakElement(self, nums) -> int:
        largest = False
        nums_len = len(nums)
        nums_len_short = nums_len - 1
        for i, num in enumerate(nums):
            # log("i:{} num:{} nums_len:{}".format(i, num, nums_len))
            if largest != False and num < largest:
                if i == 0: return 0
                return i - 1
            largest = num
            if i == nums_len_short: return i
        return 0


###################################


def test(nums, answer):
    ret = Solution().findPeakElement(nums)
    check(ret, answer, nums)


def do_all_tests():
    for i in range(1):
        test([1, 2, 3, 4, 3, 2, 1], 3)
        test([1, 2, 3, 1], 2)
        test([-2147483648], 0)
        test([1, 2], 1)
        test([-2147483648, -2147483647], 1)


if __name__ == '__main__':
    # cProfile.run('do_all_tests()', filename="/tmp/profile")
    do_all_tests()
