package main

import (
	"fmt"
	"strings"
)

func make_slices() {
	a := make([]int, 5)
	printSlice("a", a)

	b := make([]int, 5)
	printSlice("b", b)

	c := b[:2]
	printSlice("c", c)

	d := c[2:5]
	printSlice("d", d)
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}

func printSlice2(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func slices_of_slice() {
	// Create a tic-tac-toe board.
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	// The players take turns.
	board[0][0] = "X"
	board[2][2] = "0"
	board[1][2] = "X"
	board[1][0] = "0"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}

func append_example() {
	var s []int
	printSlice2(s)

	// append works on nil slices.
	s = append(s, 0)
	printSlice2(s)

	// The slice grows as needed.
	s = append(s, 1)
	printSlice2(s)

	// We can add more than one element at a time
	s = append(s, 2, 3, 4)
	printSlice2(s)
}

func main() {
	make_slices()
	slices_of_slice()
	append_example()
}
