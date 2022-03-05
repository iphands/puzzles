#!/usr/bin/env python

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def getData(arr):
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

    def addTwoNumbers(self, l1, l2):
        def itr(l):
            num = ""
            while True:
                num += str(l.val)
                if l.next == None:
                    break
                l = l.next
            return int(num[::-1])

        return Solution.getData(list(map(lambda n: int(n), str(itr(l1) + itr(l2)))))

def printNodes(head):
    while True:
        print(head.val)
        if head.next == None:
            break
        head = head.next

def test(l1, l2):
    print(printNodes(Solution().addTwoNumbers(l1, l2)))

test(Solution.getData([4,5,6]), Solution.getData([1,1,1]))
