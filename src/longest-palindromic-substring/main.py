from ..common.utils import log, check
import csv
import cProfile

class Solution:
    # Warn this is super hacktastic brute force! :D
    def longestPalindromeOld(self, s: str) -> str:
        length = len(s)
        if length < 2:
            return s

        #  check if the whole thing is a palindrome
        if self.check_string(s, length):
           return s

        for size in reversed(range(length)):
            if size == 1:
                return s[0]

            for i in range(length):
                sizei = size + i
                if sizei > length:
                    break

                if s[i] != s[sizei-1] or s[i+1] != s[sizei-2]: # fast pre-flight check
                    continue

                if self.check_string(s[i:sizei], size):
                    return s[i:sizei]

        return "foo"

    def check_string(self, s: str, size: int) -> bool:
        middle = size//2
        part1  = s[0:middle]
        part2  = s[middle:][::-1]

        if size%2:
            part1  = s[0:middle+1]

        return part1 == part2

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len < 2:
            return s

        if s_len == 2:
            if s[0] == s[1]: return s
            return s[0]

        #  check if the whole thing is a palindrome
        if self.check_string(s, s_len):
           return s

        def check_odd(start):
            r = start
            l = start

            ret = s[0]
            for i in range(1, s_len):
                l -= 1
                if l < 0:
                    l += 1
                    break

                r += 1
                if r > s_len - 1:
                    r -= 1
                    break

                # log("- start:{} r:{} l:{} s[l]:{} s[r]:{}".format(start, r, l, s[l], s[r]))
                if s[l] == s[r]:
                    ret = s[l:r+1]
                    continue
                break

            return ret

        def check_even(start):
            r = start + 1
            l = start

            if r > s_len-1 or s[r] != s[l]:
                return s[0]

            ret = s[0]
            # log("DBG {} {} {}".format(s[r], s[l], s[l:r+1]))
            if s[r] == s[l]:
                ret = s[l:r+1]

            for i in range(1, s_len):
                l -= 1
                if l < 0:
                    l += 1
                    break

                r += 1
                if r > s_len - 1:
                    r -= 1
                    break

                # log("- start:{} r:{} l:{} s[l]:{} s[r]:{}".format(start, r, l, s[l], s[r]))
                if s[l] == s[r]:
                    ret = s[l:r+1]
                    continue
                break

            # log("end start:{} r:{} l:{}".format(start, r,l))
            return ret

        ret = s[0]
        for i in range(s_len):
            # log("checking odd  from i:{} s[i]:{}".format(i, s[i]))
            result = check_odd(i)
            if len(ret) < len(result):
                ret = result

            # log("checking even from i:{} s[i]:{}".format(i, s[i]))
            result = check_even(i)
            if len(ret) < len(result):
                ret = result


        return ret

###################################


def test(s, answer):
    tmp_s = s
    if len(s) > 100:
        tmp_s = tmp_s[0:100]

    log("\n\nTesting: s:{}".format(tmp_s))
    check(Solution().longestPalindrome(s), answer, s)


def do_all_tests():
    test("babad", "bab")
    test("asdf123321fjkfjsdkaflsjfklas123321fdsfsa", "f123321f")
    test("abb", "bb")
    test("cbbd", "bb")
    with open('./src/longest-palindromic-substring/checks.dat', 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            test(row[0].strip(), row[1].strip())

if __name__ == '__main__':
    for i in range(10):
        # cProfile.run('do_all_tests()')
        do_all_tests()
