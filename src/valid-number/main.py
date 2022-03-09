all_nums = "0123456789"

# DEBUG=False
# def dbg(str):
#    if DEBUG:
#        print(str)

class Solution(object):
    def isNumber(self, s):
        l = len(s)
        if l == 1 and s in all_nums:
            return True

        seen_digit = seen_exponent = seen_dot =  False
        for i, c in enumerate(s):
            # dbg("Dbg: {} {} {} {}".format(s, i, c, s[i-1]))
            if i == 0:
                if c in "-+":
                    continue
                if c == ".":
                    seen_dot = True
                    continue

            if c in all_nums:
                seen_digit = True
                continue
            elif c in '+-':
                if s[i-1] not in "eE":
                    # dbg("# +- must follow eE")
                    return False
                if i == l-1:
                    # dbg("# +- cant be last")
                    return False
                continue
            elif c == ".":
                if seen_dot:
                    # dbg("# can only have one dot")
                    return False # can only have one dot
                if seen_exponent:
                    # dbg("# no dots after exp")
                    return False
                seen_dot = True
            elif c in 'eE':
                if not seen_digit:
                    # dbg("# exp must be after digit")
                    return False
                if seen_exponent:
                    # dbg("# can only have one exp")
                    return False
                if i == 0:
                    # dbg("# exp cant be first")
                    return False
                if i == l-1:
                    # dbg("# exp cant be last")
                    return False
                seen_exponent = True
            else:
                # dbg("# no match")
                return False

        return seen_digit

################

def test(i, ans):
    res = Solution().isNumber(i)
    if res != ans:
        print("Assertion fail: {} != {} for {}".format(res, ans, i))
        assert(False)
        return
    print("Pass:           {} == {} for {}".format(res, ans, i))

good = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", ".35", "+.8", "46.e3", "+3.e04116"]
bad = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".", "..", ".ea", "..2", ".e1", "0..", ".1.", "6+1", ".8+", "0-9", "0-", ".-4", "0+.", "5-e95", "92e1740e91", "4e+", "+E3"]

for i in good:
    test(i, True)
for i in bad:
    test(i, False)
