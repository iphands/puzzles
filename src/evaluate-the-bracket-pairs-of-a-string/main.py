from ..common.utils import log, check


class Solution:
    def evaluate(self, s, knowledge) -> str:
        k_map = {}
        for k in knowledge:
            k_map[k[0]] = k[1]

        ret = ""
        stack = ""
        capture = False
        for char in s:
            if char == "(":
                capture = True
                continue
            if char == ")":
                capture = False
                if stack in k_map:
                    ret += k_map[stack]
                else:
                    ret += "?"
                stack = ""
                continue
            if capture:
                stack += char
                continue

            ret += char

        return ret


###################################


def test(s, k, ans):
    log("\n\nTesting: s:{} k:{}".format(s, k))
    check(Solution().evaluate(s, k), ans, (s, k))


def do_all_tests():
    test("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]],
         "bobistwoyearsold")
    test("hi(name)", [["a", "b"]], "hi?")


if __name__ == '__main__':
    do_all_tests()
