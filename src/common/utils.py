from .globals import PERF, QUIET


def log(s):
    if not PERF and not QUIET:
        print(s)


def check(result, expected, inp):
    if isinstance(inp, str) and len(inp) > 100:
        inp = inp[0:100]

    if result != expected:
        s = f'Fail: result:{result} != expected:{expected} for input:{inp}'
        log(s)
        assert (False), s

    log("Pass: result:{} == expected:{} for intput:{}".format(
        result, expected, inp))


class ListNode(object):
    @staticmethod
    def from_array(arr, rev=None):
        if rev == True:
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

    def __str__(self):
        node = self
        buff = ""
        while True:
            if node.next == None:
                buff += "{} -> None".format(node.val)
                break
            buff += "{} -> ".format(node.val)
            node = node.next
        return buff

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
