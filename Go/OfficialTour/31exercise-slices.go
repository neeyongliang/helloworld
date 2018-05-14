package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	pixels := make([][]uint8, dy)
	for y := 0; y < dy; y++ {
		pixels[y] = make([]uint8, dx)
		for x := 0; x < dx; x++ {
			pixels[y][x] = uint8(x*y)
		}
	}
	return pixels
}

func main()  {
	pic.Show(Pic)
}
