package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

// or
func add2(x, y, z int) int {
	return x + y + z
}

func main() {
	fmt.Println(add(42, 13))
	fmt.Println(add2(34, 24, 8))
}
