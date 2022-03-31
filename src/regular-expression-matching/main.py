from ..common.utils import log, check


class Solution:

    def isMatch(self, s, p):
        if s == p:
            return True

        s_len = len(s)
        p_len = len(p)
        p_len_short = p_len - 1

        memo = {}

        def check(i, j):
            if (i, j) in memo:
                # log("hit memo[({}, {})]".format(i, j))
                return memo[(i, j)]

            if i >= s_len and j >= p_len:
                return True

            if j >= p_len:
                return False

            # log("check({}, {})".format(i, j))

            match = i < s_len and (s[i] == p[j] or p[j] == '.')
            in_ast = j < p_len_short and p[j + 1] == '*'

            # log("match:{}, in_ast:{}".format(match, in_ast))

            if in_ast:
                ret = check(i, j + 2) or (match and check(i + 1, j))
                memo[(i, j)] = ret
                return ret

            if match:
                ret = check(i + 1, j + 1)
                memo[(i, j)] = ret
                return ret

            return False

        return check(0, 0)


###################################


def test(s, p, answer):
    log("\n\nTesting: s:{} p:{}".format(s, p))
    check(Solution().isMatch(s, p), answer, (s, p))


def do_all_tests():
    test("aaaaaaaaaaefg", ".*efg", True)
    test("aaaaaaaaaaefg", "a*efg", True)
    test("bbbbbbefg", ".*efg", True)
    test("aa", "a", False)
    test("fdsgegabcfsde", "fdsgeg...fsde", True)
    test("aa", "a*", True)
    test("ab", ".*", True)
    test("abccdeeeeeeef", "abc.*", True)
    test("abccdeeeeeeef", "abc.*f", True)
    test("abccdeeeeeeef", "abc.*123", False)
    test("aab", "c*a*b", True)
    test("mississippi", "mis*is*ip*.", True)
    test("abcd", "d*", False)
    test("aaa", "a*a", True)
    test("aaa", "ab*a", False)
    test("aaa", "ab*a*c*a", True)
    test("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", False)


if __name__ == '__main__':
    for i in range(10240):
        do_all_tests()
