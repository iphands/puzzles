from .globals import PERF, QUIET


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def array_to_tree(arr):
    e = enumerate(arr)
    layer_i = 0
    arr_i = 1

    def get(e):
        tmp = next(e, None)
        if tmp == None:
            return None
        return tmp[1]

    layers = [[TreeNode(get(e))]]
    while arr_i < len(arr):
        layers.append([])
        layer_i += 1
        for item_i, item in enumerate(layers[layer_i - 1]):
            left_val = get(e)
            right_val = get(e)
            arr_i += 2
            left = TreeNode(left_val)
            right = TreeNode(right_val)
            item.left = left
            item.right = right
            layers[layer_i].append(left)
            layers[layer_i].append(right)

    return layers[0][0]


def tree_to_layers(head):
    layer_i = 0
    layers = [[head]]
    done = False
    while not done:
        layers.append([])
        layer_i += 1
        for item_i, item in enumerate(layers[layer_i - 1]):
            try:
                layers[layer_i].append(item.left)
                layers[layer_i].append(item.right)
            except:
                done = True
                layers = layers[0:-1 - 1]
                break

    return layers


def tree_to_answer_array(head):
    layers = tree_to_layers(head)
    ret = []
    for layer in layers:
        for item in layer:
            ret.append(item.val)
    return ret


def print_tree(head):
    layers = tree_to_layers(head)
    for layer in layers:
        log(list(map(lambda n: n.val, layer)))


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
