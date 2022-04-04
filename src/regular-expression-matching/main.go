package main

import "fmt"

var check func(i int, j int) bool

type memoItem struct {
	a int
	b int
}

func isMatch(s string, p string) bool {
	if s == p {
		return true
	}

	sLen := len(s)
	pLen := len(p)
	pLenShort := pLen - 1

	memo := make(map[(memoItem)]bool)

	check = func(i int, j int) bool {
		// fmt.Printf("DBG: i:%d j:%d sLen:%d pLen:%d\n", i, j, sLen, pLen)
		if val, ok := memo[memoItem{i, j}]; ok {
			return val
		}

		if i >= sLen && j >= pLen {
			return true
		}

		if j >= pLen {
			return false
		}

		match := i < sLen && (s[i] == p[j] || p[j] == '.')
		in_ast := j < pLenShort && p[j+1] == '*'

		if in_ast {
			ret := check(i, j+2) || (match && check(i+1, j))
			memo[memoItem{i, j}] = ret
			return ret
		}

		if match {
			ret := check(i+1, j+1)
			memo[memoItem{i, j}] = ret
			return ret
		}

		return false
	}

	return check(0, 0)
}

func test(s string, p string, ans bool) {
	fmt.Printf("\nTesting isMatch(%s, %s)\n", s, p)
	ret := isMatch(s, p)

	if ret != ans {
		panic(fmt.Sprintf("Fail: result:%t == expected:%t for intput:%s %s\n", ret, ans, s, p))
	}

	fmt.Printf("Pass: result:%t == expected:%t for intput:%s %s\n", ret, ans, s, p)
}

func main() {
	test("aaaaaaaaaaefg", ".*efg", true)
	test("aaaaaaaaaaefg", "a*efg", true)
	test("bbbbbbefg", ".*efg", true)
	test("aa", "a", false)
	test("fdsgegabcfsde", "fdsgeg...fsde", true)
	test("aa", "a*", true)
	test("ab", ".*", true)
	test("abccdeeeeeeef", "abc.*", true)
	test("abccdeeeeeeef", "abc.*f", true)
	test("abccdeeeeeeef", "abc.*123", false)
	test("aab", "c*a*b", true)
	test("mississippi", "mis*is*ip*.", true)
	test("abcd", "d*", false)
	test("aaa", "a*a", true)
	test("aaa", "ab*a", false)
	test("aaa", "ab*a*c*a", true)
	test("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c", false)

}
