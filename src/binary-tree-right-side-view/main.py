import cProfile
from ..common.utils import log, check


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if root == None:
            return

        bundle = {}
        bundle[0] = root.val

        def func(level, node):
            if node == None:
                return

            next_level = level + 1

            if node.left and node.left.val:
                bundle[next_level] = node.left.val
            if node.right and node.right.val:
                bundle[next_level] = node.right.val

            func(next_level, node.left)
            func(next_level, node.right)

        func(0, root)
        return [v for k, v in bundle.items()]


###################################


def test(inp, answer):
    log(f'\n\nTesting: inp:{inp}')

    root = TreeNode()
    left = TreeNode()
    right = TreeNode()

    for i, val in enumerate(inp):
        if i == 0:
            root.val = val
            root.left = left
            root.right = right
            continue

        if i % 2 == 0:  #even
            left.val = val
            continue
        else:
            right.val = val
            continue

    check(Solution().rightSideView(root), answer, inp)


def do_all_tests():
    test([1, None, 3], [1, 3])


def bench():
    for i in range(100):
        do_all_tests()


if __name__ == '__main__':
    # cProfile.run('bench()')
    do_all_tests()
