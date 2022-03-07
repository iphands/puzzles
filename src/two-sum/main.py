#!/usr/bin/env python

class Solution(object):
    def twoSum(self, nums, target):
        tbl = {}
        for i, num in enumerate(nums):
            tbl[num] = i

        for i, num in enumerate(nums):
            rem = target - num
            if rem in tbl:
                if tbl[rem] != i:
                    return [i, tbl[rem]]

def test(nums, target, solution):
    print("""
nums: {}
targ: {}
solu: {}
    """.format(nums, target, solution))
    assert solution[0] != solution[1]
    assert nums[solution[0]] + nums[solution[1]] == target


nums = [1,1,3,4]
target = 7
test(nums, target, Solution().twoSum(nums, target))

nums = [1,3,3]
target = 6
test(nums, target, Solution().twoSum(nums, target))

nums = [1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1]
target = 11
test(nums, target, Solution().twoSum(nums, target))
