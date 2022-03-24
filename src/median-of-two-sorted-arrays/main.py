from ..common.utils import log, check
import math


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        log("merged and sorted: {}".format(merged))
        length = len(merged)
        half_length = length / 2
        if length % 2:
            log("odd")
            return merged[int(half_length)]
        upper = int(half_length + 1) - 1
        lower = int(half_length) - 1
        log("half_length:{} upper:{} lower:{}".format(half_length, upper, lower))
        return (merged[upper] + merged[lower]) / 2


###################################


def test(nums1, nums2, answer):
    log("\n\nTesting: {} {}".format(nums1, nums2))
    check(Solution().findMedianSortedArrays(nums1, nums2), answer,
          (nums1, nums2))


def do_all_tests():
    test([1, 3], [2], 2)
    test([1, 2], [3, 4], 2.5)
    test([1, 2], [3, 4], 2.5)


if __name__ == '__main__':
    do_all_tests()
