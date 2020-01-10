package methods

import (
	"fmt"
	"math"
)

type Abser interface {
	Abs3() float64
}

type MyFloat2 float64

func (f MyFloat2) Abs3() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

func (v *Vertex3) Abs3() float64 {
	return math.Sqrt(v.X * v.X + v.Y * v.Y)
}

func TestInterfaces() {
	var a Abser
	f := MyFloat2(-math.Sqrt2)
	v := Vertex3{3, 4}
	a = f
	fmt.Println(a.Abs3())
	a = &v
	fmt.Println(a.Abs3())
}