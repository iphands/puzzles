class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 0) 2, 3
        if n == 0:
            # 4) == 1
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            # 1) 2 * -> pow(2, 2) or 4 == 8
            # 3) 4 * -> pow(4, 0) or 1 == 4
            return x * self.myPow(x, n-1)
        # 2) pow(4, 1) or 4
        return self.myPow(x*x, n/2)

#######################

PERF = False

def log(s):
    if not PERF:
        print(s)

def test(x, n, ans):
    res = Solution().myPow(x, n)
    if res != ans:
        log("Fail: {} != {} for {},{}".format(res, ans, x, n))
        # assert(False)
        return
    log("Pass: {} == {} for {},{}".format(res, ans, x, n))

def do_all_tests():
    test(2, 4, 16)
    test(2.00000, 10, 1024.00000)
    test(2.00000, 3, 8)
    test(2.00000, 2, 4)
    # test(0.00001, 2147483647, 1e-052147483647)
    pass

if PERF:
    for i in range(0, 10000):
        do_all_tests()
else:
    do_all_tests()
