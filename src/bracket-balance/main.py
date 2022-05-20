from ..common.utils import log, check


class Solution:
    def isBalanced(self, s):
        brackets = "[{()}]"
        closer = "]})"
        stack = []

        closer_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in brackets:
                if char in closer:
                    if closer_map[char] == stack[-1]:
                        stack.pop()
                    else:
                        # We can quit way early here we saw a closer with no opener on the end of the stack
                        return False
                else:
                    stack.append(char)

        return len(stack) == 0


###################################


def test(s, ans):
    log("\n\nTesting: s:{}".format(s))
    check(Solution().isBalanced(s), ans, s)


def do_all_tests():
    test("()", True)
    test("(()", False)
    test("this(is), a = {foo:bar} test(({}), a)", True)
    test("foo", True)
    test("(){([])}", True)
    test("(){(])}", False)


if __name__ == '__main__':
    do_all_tests()
