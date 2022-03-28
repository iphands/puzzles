from ..common.utils import log, check


class Solution:

    def reverse(self, x: int) -> int:
        ret = 0

        if x < 0:
            ret = -1 * int(str(x)[1:][::-1]) # marginally faster?
            # ret = -1 * int(str(-x)[::-1])
        else:
            ret = int(str(x)[::-1])

        if ret > 2147483647 or ret < -2147483648:
            return 0

        return ret


###################################


def test(x, answer):
    log("\n\nTesting: {}".format(x))
    check(Solution().reverse(x), answer, x)


def do_all_tests():
    test(123, 321)
    test(1231, 1321)
    test(-123, -321)
    test(1534236469, 0)


if __name__ == '__main__':
    for i in range(1024000):
        do_all_tests()
