from ..common.utils import log, check
import csv
import cProfile

import hashlib
memo = {}

class Solution:

    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        s_len_short = s_len - 1
        if s_len < 2:
            return s

        if s_len == 2:
            if s[0] == s[1]: return s
            return s[0]

        #  check if the whole thing is a palindrome
        if s == s[::-1]:
            return s

        key = s
        if s_len > 8:
            key = hashlib.blake2b(s.encode(), digest_size=4).hexdigest()
            # log(key)

        def check(start, is_even):
            l = start
            r = start
            if is_even:
                r = start + 1

            if r > s_len_short or s[r] != s[l]:
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
                if r > s_len_short:
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
            if (i, key) in memo:
                ret = memo[(i, key)]
                continue

            ret_len = len(ret)
            # log("checking odd  from i:{} s[i]:{}".format(i, s[i]))
            result = check(i, False)
            if ret_len < len(result):
                ret = result

            # log("checking even from i:{} s[i]:{}".format(i, s[i]))
            result = check(i, True)
            if ret_len < len(result):
                ret = result

            memo[i, key] = ret

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
    for i in range(400):
        # cProfile.run('do_all_tests()')
        do_all_tests()
