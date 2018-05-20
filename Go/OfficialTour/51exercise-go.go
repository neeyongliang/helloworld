package main

import (
	"fmt"
	"math"
)

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
	return fmt.Sprintf("cannot Sqrt negative number: %v", float64(e))
}

// 牛顿法求开方
func Sqrt2(x float64) float64 {
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

func Sqrt(x float64) (float64, error) {
	if x < 0 {
		return 0, ErrNegativeSqrt(x)
	}
	const E = 0.0000001
	res := float64(1)
	for i := 0; i < 10; i++ {
		res = res - (res*res-x)/(2*res)
	}
	return res, nil
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(Sqrt(-2))
}
