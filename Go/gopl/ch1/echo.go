// Echo1 prints its command-line arguments.
package main

import (
	"fmt"
	"os"
	"strings"
)

func echo1() {
	var s, sep string
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	fmt.Println(s)
}

func echo2() {
	fmt.Println(strings.Join(os.Args[1:], " "))
}

func main() {
	fmt.Println("--->")
	echo1()
	fmt.Println("--->")
	echo2()
}
