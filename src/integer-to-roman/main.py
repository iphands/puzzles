import cProfile
from ..common.utils import log, check

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


if __name__ == '__main__':
    # cProfile.run('do_all_tests()')
    do_all_tests()
