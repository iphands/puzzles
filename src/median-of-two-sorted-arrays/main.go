package main

import (
	"fmt"
	"sort"
)

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	merged := []int{}
	merged = append(merged, nums1...)
	merged = append(merged, nums2...)
	sort.Ints(merged)
	fmt.Printf("merged and sorted: %v\n", merged)

	length := len(merged)
	half_length := length / 2.00

	fmt.Printf("length:%v half_length:%v\n", length, half_length)

	if length%2 == 1 {
		return float64(merged[half_length])
	}

	return float64(merged[half_length]+merged[half_length-1]) / 2.00
}

func test(nums1 []int, nums2 []int, answer float64) {
	fmt.Printf("\nTesting %v %v\n", nums1, nums2)
	result := findMedianSortedArrays(nums1, nums2)
	if result != answer {
		panic(fmt.Sprintf("Fail: result:%v != expected:%v for input:%v %v", result, answer, nums1, nums2))
	}
	fmt.Printf("Pass: result:%v == expected:%v for intput:%v %v\n", result, answer, nums1, nums2)
}

func main() {
	test([]int{1, 3}, []int{2}, 2)
	test([]int{1, 2}, []int{3, 4}, 2.5)
}
