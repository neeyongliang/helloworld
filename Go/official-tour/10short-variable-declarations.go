package main

import "fmt"

func main() {
	var i, j int = 1, 2
	// := can replace var when type is clear
	// cannot use outside function
	k := 3
	c, python, java := true, false, "no!"

	fmt.Println(i, j, k, c, python, java)
}
