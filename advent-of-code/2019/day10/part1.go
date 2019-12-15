package main

import (
	"fmt"
	"io/ioutil"
	"math"
)

type asteroid [2]int

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	var asteroids []asteroid
	var x, y int
	for _, b := range data {
		switch b {
		case byte('\n'):
			x = 0
			y++
			continue
		case byte('#'):
			asteroids = append(asteroids, asteroid{x, y})
		}
		x++
	}

	var best int
	for i, a := range asteroids {
		visible := make(map[float64]bool)
		for j, b := range asteroids {
			if i == j {
				continue
			}
			φ := math.Atan2(float64(a[0]-b[0]), float64(a[1]-b[1]))
			visible[φ] = true
		}
		if len(visible) > best {
			best = len(visible)
		}
	}

	fmt.Println(best)
}
