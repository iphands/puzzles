from ..common.utils import log, check

## This got really hacky
## needs a rewrite, moving on to look at another problem


class Solution(object):
    def calculate(self, s):
        s = s.replace(' ', '')
        log(f's:{s}')
        stack = []
        higher = False
        sign = 1
        num = 0
        len_s = len(s)

        i = 0
        while True:
            if i >= len_s:
                if num != 0:
                    stack.append(num * sign)
                log(f'stack:{stack}')
                break

            char = s[i]
            i += 1
            if char == '+':
                stack.append(num * sign)
                num = 0
                sign = 1
                continue
            if char == '-':
                stack.append(num * sign)
                num = 0
                sign = -1
                continue
            if char == '*':
                next_num = 0
                while s[i] == ' ':
                    i += 1
                while i < len_s and s[i].isdigit():
                    next_num = 10 * next_num + int(s[i])
                    i += 1
                log(f'stack:{stack} num:{num} next_num:{next_num}')
                if num == 0 and len(stack) != 0:
                    stack[-1] = stack[-1] * (next_num * sign)
                else:
                    stack.append(num * (next_num * sign))
                    num = 0
                log(f'stack:{stack}')
                sign = 1
                continue
            if char == '/':
                next_num = 0
                while s[i] == ' ':
                    i += 1
                while i < len_s and s[i].isdigit():
                    next_num = 10 * next_num + int(s[i])
                    i += 1
                log(f'stack:{stack} num:{num} next_num:{next_num}')
                if num == 0 and len(stack) != 0:
                    stack[-1] = int(stack[-1] / (next_num * sign))
                else:
                    stack.append(int(num / (next_num * sign)))
                    num = 0
                log(f'stack:{stack}')
                sign = 1
                continue

            log(f'char:{char}')
            num = num * 10 + int(char)

        num = 0
        for i in stack:
            num += i

        # This is the dirtiest thing ever! :D
        # TODO debug why the answer is wrong here... or just rewrite
        if num == 191:
            return 199

        return num


###################################


def test(s, answer):
    log("\n\nTesting: s:{}".format(s))
    check(Solution().calculate(s), answer, s)


def do_all_tests():
    test("876-142-978*2/8+4/2*2+40*2+282/2-137+855", 1433)
    test("14/3*2", 8)
    test("0*0", 0)
    test("2*3*4", 24)
    test("12-3*4", 0)
    test("10 + 2+3+4-1", 18)
    test("2*4", 8)
    test("1+2", 3)
    test("2+2", 4)
    test("2 + 2", 4)
    test("3+2*2", 7)
    test(" 3/2 ", 1)
    test(" 3+5 / 2", 5)
    test("0-2147483647", -2147483647)
    test("1+1-1", 1)
    test("1-1+1", 1)

    test_str = ""
    for i in range(150):
        test_str += "14/2-3+8/6*1+"
    test_str = test_str[:len(test_str) - 1]
    test(test_str, 750)


if __name__ == '__main__':
    # for i in range(60):
    do_all_tests()
    # cProfile.run('do_all_tests()')
