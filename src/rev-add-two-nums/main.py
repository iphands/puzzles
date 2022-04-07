#!/usr/bin/env python

from ..common.utils import log, check, ListNode


def from_array(arr):
    arr.reverse()
    head = ListNode()
    l = head
    for i, item in enumerate(arr):
        l.val = item
        if i == len(arr) - 1:
            break
        l.next = ListNode()
        l = l.next

    return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        def itr(l):
            num = ""
            while True:
                num += str(l.val)
                if l.next == None:
                    break
                l = l.next
            return int(num[::-1])

        return from_array(list(map(lambda n: int(n), str(itr(l1) + itr(l2)))))


def test(l1, l2):
    print(Solution().addTwoNumbers(l1, l2))


test(ListNode.from_array([2, 4, 3]), ListNode.from_array([5, 6, 4]))
