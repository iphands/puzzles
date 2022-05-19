from ..common.utils import log, check


class Solution:
    def maxProfit(self, prices) -> int:
        min_price = 10**4
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price

            tmp = price - min_price
            if tmp > max_profit:
                max_profit = tmp

        return max_profit

    def maxProfit_old(self, prices) -> int:
        ret = 0

        for i, start in enumerate(prices):
            for end in prices[i + 1:]:
                tmp = end - start
                if ret < tmp:
                    ret = tmp

        if ret >= 0:
            return ret
        return 0


###################################


def test(prices, ans):
    log("\n\nTesting: prices:{}".format(prices))
    check(Solution().maxProfit(prices), ans, prices)


def do_all_tests():
    test([7, 1, 5, 3, 6, 4], 5)
    test([7, 6, 4, 3, 1], 0)
    test([1, 2], 1)
    test([2, 4, 1], 2)
    test([1, 1, 0], 0)


if __name__ == '__main__':
    do_all_tests()
