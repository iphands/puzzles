from ..common.utils import log, check, ListNode
import cProfile


def from_array(arr):
    head = ListNode()
    l = head
    for i, item in enumerate(arr):
        l.val = item
        if i == len(arr) - 1:
            break
        l.next = ListNode()
        l = l.next

    return head


class Solution:
    def mergeKLists(self, lists):
        if lists == []:
            return

        counts_map = {}

        def build(node):
            while True:
                if node == None:
                    return

                if node.val not in counts_map:
                    counts_map[node.val] = 0

                counts_map[node.val] += 1
                if node.next == None:
                    break

                node = node.next

        for lst in lists:
            build(lst)

        log(counts_map)
        ret_arr = []
        for key, val in sorted(counts_map.items()):
            for j in range(val):
                ret_arr.append(key)

        if ret_arr == []:
            return

        return from_array(ret_arr)


###################################


def get_nodes(arr):
    ret = []
    for a in arr:
        node = ListNode.from_array(a)
        ret.append(node)
    return ret


def test(lists_arr, answer_arr):
    lists = get_nodes(lists_arr)
    answer = ListNode.from_array(answer_arr)

    log("\n\nTesting: arr:{}".format(lists_arr))
    ret = Solution().mergeKLists(lists)
    check(str(ret), str(answer), lists_arr)


def do_all_tests():
    for i in range(10240):
        test([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])


if __name__ == '__main__':
    # cProfile.run('do_all_tests()', filename="/tmp/profile")
    do_all_tests()
