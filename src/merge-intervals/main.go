package main

import (
	"fmt"
	"reflect"
	"sort"
)

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func merge(intervals [][]int) [][]int {
	if len(intervals) < 2 {
		return intervals
	}

	sort.SliceStable(intervals, func(a int, b int) bool {
		return intervals[a][0] < intervals[b][0]
	})

	merged := [][]int{intervals[0]}
	for i, interval := range intervals {
		if i == 0 {
			continue
		}

		mlen := len(merged) - 1

		if merged[mlen][1] < interval[0] {
			merged = append(merged, interval)
			continue
		}

		merged[mlen][1] = max(merged[mlen][1], interval[1])
	}

	return merged
}

func test(input [][]int, answer [][]int) {
	result := merge(input)
	if !reflect.DeepEqual(result, answer) {
		panic(fmt.Sprintf("Fail: result:%v != expected:%v for input:%v", result, answer, input))
	}
	fmt.Printf("Pass: result:%v == expected:%v for intput:%v\n", result, answer, input)
}

func main() {
	test([][]int{{1, 3}, {2, 6}, {8, 10}, {15, 18}}, [][]int{{1, 6}, {8, 10}, {15, 18}})
	test([][]int{{1, 4}, {4, 5}}, [][]int{{1, 5}})
	test([][]int{{1, 3}}, [][]int{{1, 3}})
	test([][]int{{1, 4}, {0, 4}}, [][]int{{0, 4}})
	test([][]int{{1, 4}, {0, 5}}, [][]int{{0, 5}})
	test([][]int{{1, 4}, {2, 3}}, [][]int{{1, 4}})
	test([][]int{{1, 4}, {0, 2}, {3, 5}}, [][]int{{0, 5}})
	test([][]int{{2, 3}, {2, 2}, {3, 3}, {1, 3}, {5, 7}, {2, 2}, {4, 6}}, [][]int{{1, 3}, {4, 7}})
}
