package main

import (
	"fmt"
	"math/big"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	listToInt := func(l *ListNode) *big.Int {
		str := ""
		for true {
			str = fmt.Sprintf("%s%d", str, l.Val)

			if l.Next == nil {
				break
			}

			l = l.Next
		}

		str = reverseStr(str)

		num, ok := new(big.Int).SetString(str, 10)
		if !ok {
			panic("toobig")
		}

		return num
	}

	num := big.NewInt(0)
	num.Add(listToInt(l1), listToInt(l2))
	numStr := fmt.Sprintf("%d", num)
	numStrLen := len(numStr) - 1

	head := &ListNode{}
	curr := head
	for i, c := range reverseStr(numStr) {
		curr.Val = int(c - 48)
		if i == numStrLen {
			break
		}
		curr.Next = &ListNode{}
		curr = curr.Next
	}

	return head
}

func getData(arr []int) *ListNode {
	head := &ListNode{}
	curr := head

	for i, item := range arr {
		curr.Val = item
		if i == len(arr)-1 {
			break
		}

		curr.Next = &ListNode{}
		curr = curr.Next
	}

	return head
}

func reverse(arr []int) []int {
	ret := []int{}
	for i := len(arr) - 1; i > -1; i-- {
		ret = append(ret, arr[i])
	}
	return ret
}

func reverseStr(str string) string {
	arr := []rune(str)
	ret := []rune{}
	for i := len(arr) - 1; i > -1; i-- {
		ret = append(ret, arr[i])
	}
	return string(ret)
}

func printNodes(head *ListNode) {
	fmt.Printf("%v %v\n", head.Val, head)
	if head.Next == nil {
		return
	}

	printNodes(head.Next)
}

func main() {
	fmt.Println("Hello")
	// printNodes(getData([]int{1, 2, 3}))
	l1 := getData([]int{2, 4, 9})
	l2 := getData([]int{5, 6, 4, 9})
	printNodes(addTwoNumbers(l1, l2))

	// [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
	// [5,6,4]

	l1 = getData([]int{1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1})
	l2 = getData([]int{5, 6, 4})
	printNodes(addTwoNumbers(l1, l2))
}
