from ..common.utils import log, check


class Solution:
    def wiggleSort(self, nums) -> None:
        nums_len = len(nums)
        if nums_len == 1:
            return

        nums_sorted = sorted(nums)
        nums_half_len = (nums_len / 2) + 2

        i = 0
        while True:
            l = len(nums_sorted)
            if l > 1:
                nums[i] = nums_sorted[0]
                nums[i + 1] = nums_sorted.pop()
                del nums_sorted[0]
                i += 2
            else:
                if l > 0:
                    nums[i] = nums_sorted[0]
                return


###################################


def test(nums, ans):
    log("\n\nTesting: nums:{}".format(nums))
    tmp = nums.copy()
    Solution().wiggleSort(tmp)
    check(tmp, ans, nums)


def do_all_tests():
    test([3, 5, 2, 1, 6, 4], [1, 6, 2, 5, 3, 4])
    test([0, 0], [0, 0])
    test([1, 1, 1], [1, 1, 1])


if __name__ == '__main__':
    do_all_tests()
