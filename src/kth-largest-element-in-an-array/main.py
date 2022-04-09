from ..common.utils import log, check


class Solution(object):
    def findKthLargest(self, nums, k) -> int:
        return sorted(nums)[::-1][k - 1]


###################################


def test(nums, k, answer):
    log("\n\nTesting: nums:{} k:{}".format(nums, k))
    check(Solution().findKthLargest(nums, k), answer, (nums, k))


def do_all_tests():
    test([1, 2, 3, 4], 2, 3)
    test([3, 2, 1, 5, 6, 4], 2, 5)
    test([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)


if __name__ == '__main__':
    do_all_tests()
