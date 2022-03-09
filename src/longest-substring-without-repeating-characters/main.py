class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ret = 0
        l = len(s)

        if l == 1:
            return 1

        for i in range(0, l - 1):
            found = untilUniq("", s[i:l])
            if found > ret:
                ret = found

        # print("Dbg: found \"{}\" count {}".format(found, len(found)))
        return ret

def untilUniq(found, s):
    # print("Dbg: found: \"{}\" s: {}".format(found, s))
    newFound = found
    for i in s:
        if i in newFound:
            # print(" f: {}".format(i))
            return len(newFound)
        # print("nf: {}".format(i))
        newFound += i
    return untilUniq(newFound, s[1:len(s)])

assert(Solution().lengthOfLongestSubstring("abcabcbb") == 3)
assert(Solution().lengthOfLongestSubstring("bbbb") == 1)
assert(Solution().lengthOfLongestSubstring("pwwkew") == 3)
assert(Solution().lengthOfLongestSubstring(" ") == 1)
