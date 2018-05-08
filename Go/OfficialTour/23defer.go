package main

import "fmt"

func defer_example() {
	defer fmt.Println("world")

	fmt.Println("hello")
}

func defer_multi() {
	fmt.Println("counting")

	for i := 0; i < 10; i ++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
}

func main() {
	defer_example()
	defer_multi()
}
