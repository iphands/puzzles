from ..common.utils import log, check


def getTrappedRainWater(arr):
    arr_len = len(arr)

    max_left = 0
    max_right = 0

    left = 0
    right = arr_len - 1

    total = 0

    while left < right:
        hleft = arr[left]
        hright = arr[right]

        if hleft < hright:
            if hleft >= max_left:
                # cant add water here
                max_left = hleft
            else:
                total += max_left - hleft
            left += 1
        else:
            if hright >= max_right:
                max_right = hright
            else:
                total += max_right - hright
            right -= 1

    return total


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, ' Test #', test_case_number, sep='')
    else:
        print(wrongTick,
              ' Test #',
              test_case_number,
              ': Expected ',
              expected,
              sep='',
              end='')
        print(' Your output: ', output, end='')
        print()
    test_case_number += 1


if __name__ == "__main__":
    outputOne = getTrappedRainWater([7, 4, 0, 9])
    check(10, outputOne)
    outputTwo = getTrappedRainWater([6, 9, 9])
    check(0, outputTwo)
    # Add your own test cases here
