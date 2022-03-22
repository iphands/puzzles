from .globals import PERF, QUIET

def log(s):
    if not PERF and not QUIET:
        print(s)

def check(result, expected, inp):
    if result != expected:
        print("Fail: result:{} != expected:{} for input:{}".format(result, expected, inp))
        assert(False)
    print("Pass: result:{} == expected:{} for intput:{}".format(result, expected, inp))
