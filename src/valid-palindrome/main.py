from ..common.utils import log, check, ListNode
import cProfile

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]

###################################


def test(s, answer):
    ret = Solution().isPalindrome(s)
    check(ret, answer, s)


def do_all_tests():
    for i in range(1):
        test("A man, a plan, a canal: Panama", True)
        test("0P", False)


if __name__ == '__main__':
    # cProfile.run('do_all_tests()', filename="/tmp/profile")
    do_all_tests()
