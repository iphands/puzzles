from ..common.utils import log, check


class Solution:
    def simplifyPath(self, path):
        tokens = list(filter(None, path.split("/")))
        log("tokens:{}".format(tokens))

        ret = []
        for i, token in enumerate(tokens):
            if token == '..':
                if len(ret):
                    ret.pop()
                continue
            if token == '.':
                continue
            ret.append(token)

        return '/' + '/'.join(ret)


###################################


def test(path, ans):
    log("\n\nTesting: path:{}".format(path))
    check(Solution().simplifyPath(path), ans, path)


def do_all_tests():
    test("/home/", "/home")
    test("/home/iphands/..", "/home")
    test("/../", "/")
    test("/a/./b/../../c/", "/c")


if __name__ == '__main__':
    for i in range(1):
        do_all_tests()
