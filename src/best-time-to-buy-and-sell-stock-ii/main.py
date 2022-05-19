from ..common.utils import log, check


class Solution:
    def find(self, prices):
        stack = []
        current = prices[0]
        direction = 0
        old_direction = 0
        prices_len = len(prices) - 1

        for i, price in enumerate(prices):
            if i == prices_len:
                if len(stack) != 0 and stack[-1] < price:
                    stack.append(price)
                break

            nxt = prices[i + 1]
            diff = nxt - price
            if diff > 0:
                direction = 1
            elif diff < 0:
                direction = -1
            else:
                continue

            if direction > old_direction:
                stack.append(price * -1)
            elif direction < old_direction:
                stack.append(price)

            old_direction = direction

        log(f'stack:{stack}')
        return stack

    def maxProfit(self, prices) -> int:
        prices_len = len(prices)
        if prices_len == 0 or prices_len == 1:
            return 0

        started = False
        total = 0
        stack = self.find(prices)
        for i in stack:
            log(f'total:{total}')
            if i <= 0:  ## this is some BS price of $0 lolol
                log(f'buying at {i}')
                total += i  # buy
                started = True
            elif started:
                log(f'selling at {i}')
                total += i

        return total


###################################


def test(prices, ans):
    log("\n\nTesting: prices:{}".format(prices))
    check(Solution().maxProfit(prices), ans, prices)


def do_all_tests():
    test([7, 1, 5, 3, 6, 4], 7)
    test([1, 2, 3, 4, 5], 4)
    test([6, 1, 3, 2, 4, 7], 7)
    test([5, 7, 2, 7, 3, 3, 5, 3, 0], 9)
    test([0, 3, 8, 6, 8, 6, 6, 8, 2, 0, 2, 7], 19)
    test([1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9], 25)


if __name__ == '__main__':
    do_all_tests()
