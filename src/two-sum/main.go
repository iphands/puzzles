package main

import "fmt"

func twoSum(nums []int, target int) []int {
	tbl := make(map[int]int)
	for i, num := range(nums) {
		tbl[num] = i
	}

	for i, num := range(nums) {
		rem := target - num
		if _, ok := tbl[rem]; ok {
			if tbl[rem] != i {
				return []int{i, tbl[rem]}
			}
		}
	}

	return []int{0,0}
}

func main() {
	fmt.Println("test")
	fmt.Printf("TEST: %v\n", twoSum([]int{1,2,3,4}, 7))
	fmt.Printf("TEST: %v\n", twoSum([]int{1,3,3}, 6))
	fmt.Printf("TEST: %v\n", twoSum([]int{1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1}, 11))
}
