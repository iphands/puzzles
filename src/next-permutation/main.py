#!/usr/bin/env python

class Solution(object):
    @staticmethod
    def isLargest(lst):
        for i, num in enumerate(lst):
            if i == 0: continue
            if lst[i-1] < num:
                return False
        return True

    @staticmethod
    def findLesser(lst):
        last = lst[-1]
        for i, num in reversed(list(enumerate(lst))):
            if last > num:
                return i
            last = num
        assert(False)

    @staticmethod
    def findNextLargest(lst):
        ret = (1000000000, 0) # this leading number is naughty
        for i, num in enumerate(lst):
            # print("DEBUG: lst:{} ret:{} num:{}".format(lst, ret, num))
            if num > lst[0] and num <= ret[0]:
                ret = (num, i)
        return ret[1]

    @staticmethod
    def swap(lst, s1, s2):
        tmp = lst[s2]
        lst[s2] = lst[s1]
        lst[s1] = tmp

    @staticmethod
    def reverse(lst, start):
        sub_list = lst[start+1:]
        if len(sub_list) == 1:
            # print("DEBUG0: lst:{} sub:{} start:{}".format(lst, sub_list, start))
            return

        # print("DEBUG1: lst:{} sub{}:".format(lst, sub_list))
        sub_list.reverse()
        # print("DEBUG2: lst:{} sub{}:".format(lst, sub_list))
        for i, num in enumerate(sub_list):
            lst[i + start + 1] = num
        # print("DEBUG3: lst:{} sub{}:".format(lst, sub_list))

    def nextPermutation(self, nums):
        if self.isLargest(nums):
            return nums.sort()

        swap1 = self.findLesser(nums)
        swap2 = self.findNextLargest(nums[swap1:]) + swap1
        # print("DEBUG: {} {}".format(swap1, swap2))
        self.swap(nums, swap1, swap2)
        self.reverse(nums, swap1)

        return None

#######################

SHH = True

def log(s):
    if not SHH:
        print(s)

def test(l, ans):
    res = l.copy()
    Solution().nextPermutation(res)
    if res != ans:
        log("Fail: {} != {} for {}".format(res, ans, l))
        assert(False)
        return
    log("Pass: {} == {} for {}".format(res, ans, l))

for i in range(0, 100000):
    test([1,2,3], [1,3,2])
    test([2,3,1], [3,1,2])
    test([1,1,5], [1,5,1])
    test([3,2,1], [1,2,3])
    test([1,2,3,4], [1,2,4,3])
    test([1,2], [2,1])
    test([1,3,2], [2,1,3])
    test([3,1,2], [3,2,1])
    test([2,3,1,3,3], [2,3,3,1,3])
