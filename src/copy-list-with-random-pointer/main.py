from ..common.utils import log, check
import random


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def getList(self, head):
        last = head
        prev = None
        i = 0

        ret = []
        while last != None:
            if i != 0:
                prev.next = head

            head.id = i
            last = last.next
            prev = head

            ret.append(head)
            head = head.next
            i += 1

        return ret

    def copyRandomList(self, head):
        if head == None:
            return None

        if head.next == None:
            ret = Node(head.val)
            if head.random != None:
                ret.random = ret
            return ret

        old_lst = self.getList(head)
        new_list = []

        for item in old_lst:
            node = Node(item.val)
            node.id = item.id
            new_list.append(node)

        for item in old_lst:
            if item.next != None:
                new_list[item.id].next = new_list[item.next.id]

            if item.random != None:
                new_list[item.id].random = new_list[item.random.id]

        return new_list[0]


###################################


def test():
    root = Node(1)
    last = root

    arr = [root]
    for i in range(10):
        node = Node(i)
        arr.append(node)
        last.next = node
        last = node

    for n in arr:
        i = random.randint(0, 9)
        n.random = arr[i]

    ans = Solution().copyRandomList(root)
    last = ans
    i = 0

    while last != None:
        log(f'input:{arr[i].val} last:{last.val}')
        assert (last.val == arr[i].val)
        if arr[i].next != None:
            assert (last.next != None)

        last = last.next
        i += 1


def do_all_tests():
    test()


if __name__ == '__main__':
    do_all_tests()
    # cProfile.run('do_all_tests()')
