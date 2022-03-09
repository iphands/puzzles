package main

import (
	"fmt"
	"strings"
)

func isNumber(s string) bool {
	all_nums := "0123456789"
	l := len(s)

	if l == 1 && strings.Contains(all_nums, s) {
		return true
	}

	seen_digit := false
	seen_exponent := false
	seen_dot := false

	for i, r := range s {
		c := string(r)

		if i == 0 {
			if strings.Contains("-+", c) {
				continue
			}

			if c == "." {
				seen_dot = true
				continue
			}
		}

		if strings.Contains(all_nums, c) {
			seen_digit = true
			continue
		} else if strings.Contains("+-", c) {
			if !strings.Contains("eE", string(s[i-1])) {
				// dbg("# +- must follow eE")
				return false
			}
			if i == l-1 {
				// dbg("# +- cant be last")
				return false
			}
			continue
		} else if c == "." {
			if seen_dot {
				// dbg("# can only have one dot")
				return false
			}
			if seen_exponent {
				// dbg("# no dots after exp")
				return false
			}
			seen_dot = true
		} else if strings.Contains("eE", c) {
			if !seen_digit {
				// dbg("# exp must be after digit")
				return false
			}
			if seen_exponent {
				// dbg("# can only have one exp")
				return false
			}
			if i == 0 {
				// dbg("# exp cant be first")
				return false
			}
			if i == l-1 {
				// dbg("# exp cant be last")
				return false
			}
			seen_exponent = true
		} else {
			// dbg("# no match")
			return false
		}
	}

	return seen_digit
}

///////////////////////

func dbg(s string) {
	fmt.Println(s)
}

func test(i string, ans bool) {
	res := isNumber(i)
	if res != ans {
		panic(fmt.Sprintf("Fail: %t != %t for %s\n", res, ans, i))
	}

	fmt.Printf("Pass: %t == %t for %s\n", res, ans, i)
}

func main() {
	good := []string{"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", ".35", "+.8", "46.e3", "+3.e04116"}
	bad := []string{"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".", "..", ".ea", "..2", ".e1", "0..", ".1.", "6+1", ".8+", "0-9", "0-", ".-4", "0+.", "5-e95", "92e1740e91", "4e+", "+E3"}

	for _, i := range good {
		test(i, true)
	}

	for _, i := range bad {
		test(i, false)
	}
}
