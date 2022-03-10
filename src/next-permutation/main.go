package main

import (
	"fmt"
	"reflect"
)

func reverseInPlace(nums *[]int) {
	numsLen := len(*nums)
	numsLenSubOne := numsLen - 1
	orig := make([]int, numsLen)
	copy(orig, *nums)

	for i := 0; i < numsLen; i += 1 {
		(*nums)[numsLenSubOne-i] = orig[i]
	}
}

func reversePartial(lst *[]int, start int) {
	lstLen := len(*lst)
	if lstLen-start == 1 {
		return
	}

	subList := (*lst)[start+1:]
	reverseInPlace(&subList)
}

func reverse(nums []int) []int {
	numsLen := len(nums)
	numsLenSubOne := numsLen - 1
	tmp := make([]int, numsLen)
	copy(tmp, nums)

	for i := 0; i < numsLen; i += 1 {
		tmp[numsLenSubOne-i] = nums[i]
	}

	return tmp
}

func isLargest(nums []int) bool {
	for i, num := range nums {
		if i == 0 {
			continue
		}

		if nums[i-1] < num {
			return false
		}
	}

	return true
}

func findLesser(lst []int) int {
	lstLen := len(lst)
	last := lst[lstLen-1]
	for idx, num := range reverse(lst) {
		i := lstLen - 1 - idx // The list and the index needs to be reversed here
		if last > num {
			return i
		}
		last = num
	}
	panic("Did not find lesser")
}

func findNextLargest(lst []int) int {
	curr := 1000000
	ret := 0
	for i, num := range lst {
		if num > lst[0] && num <= curr {
			curr = num
			ret = i
		}
	}

	return ret
}

func swap(lst *[]int, s1 int, s2 int) {
	tmp := (*lst)[s2]
	(*lst)[s2] = (*lst)[s1]
	(*lst)[s1] = tmp
}

func nextPermutation(nums []int) {
	if isLargest(nums) {
		reverseInPlace(&nums)
		return
	}

	swap1 := findLesser(nums)
	swap2 := findNextLargest(nums[swap1:]) + swap1
	swap(&nums, swap1, swap2)
	reversePartial(&nums, swap1)

	return
}

func log(s string) {
	fmt.Println(s)
}

func test(l []int, ans []int) {
	orig := make([]int, len(l))
	copy(orig, l)

	nextPermutation(l)
	if !reflect.DeepEqual(l, ans) {
		log(fmt.Sprintf("Fail: res:%v != ans:%v for orig:%v", l, ans, orig))
		// panic("ZOMG")
	}

	log(fmt.Sprintf("Pass: res:%v != ans:%v for orig:%v", l, ans, orig))
}

func doAllTests() {
	test([]int{1, 2, 3}, []int{1, 3, 2})
	test([]int{2, 3, 1}, []int{3, 1, 2})
	test([]int{1, 1, 5}, []int{1, 5, 1})
	test([]int{3, 2, 1}, []int{1, 2, 3})
	test([]int{1, 2, 3, 4}, []int{1, 2, 4, 3})
	test([]int{1, 2}, []int{2, 1})
	test([]int{1, 3, 2}, []int{2, 1, 3})
	test([]int{3, 1, 2}, []int{3, 2, 1})
	test([]int{2, 3, 1, 3, 3}, []int{2, 3, 3, 1, 3})
	test([]int{4, 3, 2, 1}, []int{1, 2, 3, 4})
	test([]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5})
}

func main() {
	doAllTests()
}
