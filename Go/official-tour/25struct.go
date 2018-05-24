package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	p  = &Vertex{1, 2} // has type *Vertex
)

func main() {
	v := Vertex{1, 2}
	fmt.Println(v)

	// struct fields
	v.Y = 4
	fmt.Println(v)

	// struct pointers
	p := &v
	p.X = 1e9
	fmt.Println(v)

	// struct literals
	fmt.Println(v1, p, v2, v3)
}
