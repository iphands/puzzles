package main

import (
	"fmt"
	"strings"
)

func lengthOfLongestSubstring(s string) int {
	ret := 0
	l := len(s)
	l1 := l - 1

	if l == 1 {
		return 1
	}

	for i := 0; i < l1; i += 1 {
		found := untilUniq("", s[i:])
		if found > ret {
			ret = found
		}
	}

	return ret
}

func untilUniq(found string, s string) int {
	newFound := found
	for _, i := range s {
		if (strings.ContainsRune(newFound, i)) {
			return len(newFound)
		}
		newFound += string(i)
	}

	return untilUniq(newFound, s[1:])
}

//////

func assert(num1 int, num2 int) {
	if num1 != num2 {
		panic(fmt.Sprintf("Assertion failed: %d != %d", num1, num2))
	}
}

func main() {
	assert(lengthOfLongestSubstring("abcabcbb"), 3)
	assert(lengthOfLongestSubstring("bbbb"), 1)
	assert(lengthOfLongestSubstring("pwwkew"), 3)
	assert(lengthOfLongestSubstring(" "), 1)
	assert(lengthOfLongestSubstring(""), 0)
}
