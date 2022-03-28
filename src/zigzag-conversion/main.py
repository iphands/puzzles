from ..common.utils import log, check


class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        numRowsShort = numRows - 1
        matrix = []
        for i in range(numRows):
            matrix.append([])

        slot_i = 0
        modifier = 1
        for i, c in enumerate(s):
            log("i:{} c:{} slot_i:{}".format(i, c, slot_i))

            matrix[slot_i].append(c)

            if slot_i >= numRowsShort:
                modifier = -1

            if slot_i <= 0:
                modifier = 1

            slot_i += modifier

        ret = ""
        for i in range(numRows):
            log("adding: {} to ret:{}".format(matrix[i], ret))
            ret += ''.join(matrix[i])

        log("ret:{}".format(ret))
        return ret


###################################


def test(s, numRows, answer):
    log("\n\nTesting: {}".format(s))
    check(Solution().convert(s, numRows), answer, (s))


def do_all_tests():
    test("A", 1, "A")
    test("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")
    test("PAYPALISHIRING", 4, "PINALSIGYAHRPI")


if __name__ == '__main__':
    for i in range(10):
        do_all_tests()
