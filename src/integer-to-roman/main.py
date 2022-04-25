import cProfile
from ..common.utils import log, check

#  all possible 1,4,5,9
i_to_rn = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I',
}


class Solution:
    def intToRoman(self, num: int) -> str:
        # ret = []
        ret = ""

        for n, rn in i_to_rn.items():
            # log(f'using n:{n} rnum:{rn}')
            while num >= n:
                num = num - n
                # ret.append(rn)
                ret += rn

        # return "".join(ret)
        return ret


###################################


def test(num, answer):
    log(f'\n\nTesting: num:{num}')
    check(Solution().intToRoman(num), answer, num)


def do_all_tests():
    test(3724, 'MMMDCCXXIV')
    test(1, 'I')
    test(2, 'II')
    test(3, 'III')
    test(4, 'IV')
    test(5, 'V')
    test(1994, 'MCMXCIV')
    with open('./src/integer-to-roman/data.csv', 'r') as f:
        for line in f.readlines():
            num, rnum = line.strip().split(',')
            test(int(num), rnum)


def bench():
    for i in range(100):
        do_all_tests()


if __name__ == '__main__':
    # cProfile.run('bench()')
    do_all_tests()
