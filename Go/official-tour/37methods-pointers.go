package main

import (
    "fmt"
    "math"
)

type Vertex struct {
    X, Y float64
}

func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// 指针接收者的方法可以修改接收者指向的值（就像 Scale 在这做的）。
// 由于方法经常需要修改它的接收者，指针接收者比值接收者更常用。
func (v *Vertex) Scale(f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}

func method_pointers_example() {
    v := Vertex{3, 4}
    v.Scale(10)
    fmt.Println(v.Abs())
}

func Abs2(v Vertex) float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func Scale2(v *Vertex, f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}

func method_pointers_explained() {
    v := Vertex{3, 4}
    Scale2(&v, 10)
    fmt.Println(Abs2(v))
}

func main() {
    method_pointers_example()
    method_pointers_explained()
}
