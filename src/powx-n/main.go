package main

import (
	"fmt"
	"math"
)

func myPow(x float64, n int) float64 {
	// if exp is 0 return 1
	if n == 0 {
		return 1.0
	}

	// n ^ 1 is always n
	if n == 1 {
		return x
	}

	// if n is negative use 1/-n
	if n < 0 {
		return 1 / myPow(x, n*-1)
	}

	// if n is even
	if n%2 == 1 {
		return x * myPow(x, n-1)
	}

	// if n is odd
	return myPow(x*x, n/2)
}

func check(x float64, n int) float64 {
	return math.Pow(x, float64(n))
}

func test(x float64, n int) {
	actual := check(x, n)
	result := myPow(x, n)
	if result != actual {
		panic(fmt.Sprintf("Error res:%f != act:%f", result, actual))
	}

	fmt.Printf("Pass %f == %f for %f^%d\n", result, actual, x, n)
}

func main() {
	test(2.0, 3)
	test(2, 4)
	test(2.00000, 10)
	test(2.00000, 3)
	test(2.00000, 2)
	test(0.00001, 2147483647)
}
