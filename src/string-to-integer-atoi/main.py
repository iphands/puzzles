from ..common.utils import log, check

char_map = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


class Solution:

    def myAtoi(self, s: str) -> int:
        s_len = len(s)

        if s_len == 0:
            return 0

        idx = 0
        signer = 1

        # trim off beginning
        while idx < s_len:
            if s[idx] == ' ':
                idx += 1
                continue
            if s[idx] == '+':
                idx += 1
                break
            if s[idx] == '-':
                signer = -1
                idx += 1
                break
            if s[idx] >= '0' and s[idx] <= '9':
                break
            return 0

        log("first num at idx:{}".format(idx))

        nums = ""
        # nums = []
        while idx < s_len and s[idx] >= '0' and s[idx] <= '9':
            log("Num part s[idx]:{}".format(s[idx]))
            nums += s[idx]
            # nums.append(s[idx])
            idx += 1

        ret = 0
        for i, char in enumerate(nums[::-1]):
            log("i:{} char:{}".format(i, char))
            # ret += (ord(char) - 48) * (10**i)
            ret += char_map[char] * (10**i)

        if ret > 2147483647:
            return 2147483647 * signer

        return ret * signer


###################################


def test(x, answer):
    log("\n\nTesting: {}".format(x))
    check(Solution().myAtoi(x), answer, x)


def do_all_tests():
    test("123", 123)
    test("1230", 1230)
    test("-123", -123)
    test(" +123", 123)
    test("  -123", -123)
    test("321 sadf fdsaf 123", 321)
    test("+-12", 0)
    test("  -0012a42", -12)
    test("00000-42a1234", 0)
    test("-5-", -5)


if __name__ == '__main__':
    for i in range(300000):
        do_all_tests()
