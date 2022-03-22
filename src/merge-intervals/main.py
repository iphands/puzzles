from ..common.utils import log, check


class Solution(object):

    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        log("Sorted: {}".format(intervals))

        merged = []
        for interv in intervals:
            log("Testing {} and {}".format(interv, merged))
            if not merged:
                merged.append(interv)
                continue

            if merged[-1][1] < interv[0]:
                log("No overlap: {} {}".format(interv, merged[-1]))
                log("   merged[-1][1] {} < interv[0] {}".format(merged[-1][1], interv[0]))
                merged.append(interv)
                continue

            log("Overlap: {} {}".format(interv, merged[-1]))
            merged[-1][1] = max(merged[-1][1], interv[1])

        return merged


###################################


def test(inp, answer):
    log("\n\nTesting: {}".format(inp))
    check(Solution().merge(inp), answer, inp)


def do_all_tests():
    test([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])
    test([[1, 4], [4, 5]], [[1, 5]])
    test([[1, 3]], [[1, 3]])
    test([[1, 4], [0, 4]], [[0, 4]])
    test([[1, 4], [0, 5]], [[0, 5]])
    test([[1, 4], [2, 3]], [[1, 4]])
    test([[1, 4], [0, 2], [3, 5]], [[0, 5]])
    test([[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]],
         [[1, 3], [4, 7]])


if __name__ == '__main__':
    do_all_tests()
