from ..common.utils import log, check


class Solution:
    def merge(self, nums1, m, nums2, n):
        counts_map = {}

        def build(nums, nums_count):
            for i, num in enumerate(nums):
                if i == nums_count:
                    break
                if num not in counts_map:
                    counts_map[num] = 0
                counts_map[num] += 1

        build(nums1, m)
        build(nums2, n)
        # log(counts_map)
        i = 0
        for key, val in sorted(counts_map.items()):
            for j in range(val):
                nums1[i] = key
                # log(nums1)
                i += 1


###################################


def test(nums1, m, nums2, n, answer):
    orig = nums1.copy()
    log("\n\nTesting: nums1:{} m:{} nums2{} n:{}".format(nums1, m, nums2, n))
    Solution().merge(nums1, m, nums2, n)
    check(nums1, answer, (orig, m, nums2, n))


def do_all_tests():
    test([2, 0], 1, [1], 1, [1, 2])
    test([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6])
    test([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3,
         [-1, 0, 0, 1, 2, 2, 3, 3, 3])


if __name__ == '__main__':
    for i in range(1):
        do_all_tests()
