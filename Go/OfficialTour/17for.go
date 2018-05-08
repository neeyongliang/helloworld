package main

import "fmt"

func for_1() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}

func for_2() {
	sum := 1
	for ; sum < 1000; {
		sum += sum
	}
	fmt.Println(sum)
}

func for_is_while() {
	sum := 1
	// C's while is Go's for
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}

func for_forever() {
	for {
		// will not stop automatic
	}
}

func main() {
	for_1()
	for_2()
	for_is_while()
}
