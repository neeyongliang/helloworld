package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	const E = 0.000001
	z := float64(1)
	k := float64(0)
	for ; ; z = z - (z*z-x)/(2*z) {
		if math.Abs(z-k) <= E {
			return z
		}
		fmt.Println(z)
		k = z
	}
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(math.Sqrt(2))
}
