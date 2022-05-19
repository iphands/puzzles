from ..common.utils import log, check, array_to_tree, print_tree, tree_to_answer_array


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
        def find(node, target, stack):
            if node == None:
                return

            stack.append(node)

            if node and node.left and node.left.val == target.val:
                stack.append(node.left)
                return stack

            if node and node.right and node.right.val == target.val:
                stack.append(node.right)
                return stack

            ret = find(node.left, target, stack.copy())
            if ret != None:
                return ret

            ret = find(node.right, target, stack.copy())
            if ret != None:
                return ret

        p_stack = find(root, p, [])
        q_stack = find(root, q, [])

        if p_stack == None:
            p_stack = [root]

        if q_stack == None:
            q_stack = [root]

        log(list(map(lambda n: n.val, p_stack)))
        log(list(map(lambda n: n.val, q_stack)))

        for i in reversed(p_stack):
            if i in q_stack:
                return i


###################################


def test(head, p, q, answer):
    in_safe = tree_to_answer_array(head)

    p_node = TreeNode(p)
    q_node = TreeNode(q)

    log("\n\nTesting: {} {} {}".format(in_safe, p, q))
    check(Solution().lowestCommonAncestor(head, p_node, q_node).val, answer,
          (in_safe, p, q))


def do_all_tests():
    head = array_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    test(head, 5, 1, 3)

    head = array_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    test(head, 5, 4, 5)

    head = array_to_tree([1, 2])
    test(head, 1, 2, 1)

    head = array_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    test(head, 6, 0, 3)


if __name__ == '__main__':
    do_all_tests()
