from ..common.utils import log, check


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root) -> int:
        def get_num(num, node, parent, left):
            log(f'num:{num} nums:{nums}')
            num = num * 10 + node.val
            node.leaf = True
            if node.left != None:
                log(f'going left num:{num}')
                node.leaf = False
                get_num(num, node.left, node, True)
            if node.right != None:
                log(f'going right num:{num}')
                node.leaf = False
                get_num(num, node.right, node, False)

            if parent:
                if left:
                    parent.left = None
                else:
                    parent.right = None

            parent = None
            log(f'leaf:{node.leaf}\n')
            if node.leaf:
                nums.append(num)

        nums = []
        get_num(0, root, None, True)
        log(f'nums:{nums}')
        return sum(nums)


###################################


def test(root, answer):
    log(f'\n\nTesting: root:{root}')
    check(Solution().sumNumbers(root), answer, [4, 9, 0, 5, 1])


def do_all_tests():
    root = TreeNode(val=4)
    root.left = TreeNode(val=9)
    root.left.left = TreeNode(val=5)
    root.left.right = TreeNode(val=1)
    root.right = TreeNode(val=0)

    test(root, 1026)


if __name__ == '__main__':
    # for i in range(60):
    do_all_tests()
    # cProfile.run('do_all_tests()')
