from ..common.utils import log, check
import csv
import cProfile

class Solution:
    def check_string(self, s: str, size: int) -> bool:
        middle = size//2
        part2  = s[middle:][::-1]

        if size%2:
            part1  = s[0:middle+1]
            return part1 == part2

        part1  = s[0:middle]
        return part1 == part2

    # Warn this is super hacktastic brute force! :D
    def longestPalindrome(self, s: str) -> str:
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
                substr = s[i:sizei]

                if (substr[0] != substr[-1] or substr[1] != substr[-2]): # fast pre-flight check
                    continue

                if self.check_string(substr, size):
                    return substr

        return "foo"


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

    with open('./src/longest-palindromic-substring/checks.dat', 'r') as data:
        reader = csv.reader(data)
        for row in reader:
            test(row[0].strip(), row[1].strip())

if __name__ == '__main__':
    for i in range(10):
        cProfile.run('do_all_tests()')
        # do_all_tests()
