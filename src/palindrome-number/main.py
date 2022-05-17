from ..common.utils import log, check


class Solution:

    def isPalindrome(self, x):
        if x < 0: return False
        if x < 10: return True

        x_str = str(x)

        # return x_str == x_str[::-1] # Heh

        x_len = len(x_str)
        x_len_minus_one = x_len - 1
        middle = x_len // 2

        for i in range(middle):
            if x_str[i] != x_str[x_len_minus_one - i]:
                return False
        return True


###################################


def test(x, answer):
    log("\n\nTesting: {}".format(x))
    check(Solution().isPalindrome(x), answer, x)


def do_all_tests():
    test(1, True)
    test(2, True)
    test(0, True)
    test(121, True)
    test(134, False)
    test(1221, True)
    test(1234554321, True)
    test(123454675474, False)


if __name__ == '__main__':
    # for i in range(300000):
    do_all_tests()
