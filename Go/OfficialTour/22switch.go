package main

import (
	"fmt"
	"runtime"
	"time"
)

func switch_example() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
		// fallthrough
	default:
		// freebsd, openbsd
		// plan9, windows...
		fmt.Printf("-->%s", os)
	}
}

func switch_evaluation_order() {
	fmt.Println("When's wednesday")
	today := time.Now().Weekday()
	switch time.Wednesday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow.")
	case today + 2:
		fmt.Println("In two days.")
	default:
		fmt.Println("Too far away.")
	}
}

func switch_with_no_condition() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening")
	}
}

// itself use break, if want forbid, use fallthrough
func main() {
	switch_example()
	switch_evaluation_order()
	switch_with_no_condition()
}
