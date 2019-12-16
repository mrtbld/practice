package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"sort"
)

const TARGET = 200

type asteroid [2]int
type visibilityMap map[float64][]float64

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

	var station asteroid
	var vis visibilityMap
	for i, a := range asteroids {
		vm := make(visibilityMap)
		for j, b := range asteroids {
			if i == j {
				continue
			}
			x, y := float64(b[0]-a[0]), float64(b[1]-a[1])
			φ := math.Atan2(y, x)
			r := math.Sqrt(x*x + y*y)
			vm[φ] = append(vm[φ], r)
		}
		if len(vm) > len(vis) {
			station = a
			vis = vm
		}
	}

	φs := make([]float64, len(vis))
	i := 0
	for φ, r := range vis {
		sort.Float64s(r)
		φs[i] = φ
		i++
	}
	sort.Float64s(φs)

	var up int
	for i, φ := range φs {
		if φ >= -math.Pi/2 {
			up = i
			break
		}
	}

	for i, j := 0, up; i < len(asteroids)-1; i, j = i+1, j+1 {
		φ := φs[j%len(φs)]
		if len(vis[φ]) == 0 {
			i--
			continue
		}
		if i+1 == TARGET {
			r := vis[φ][0]
			x := station[0] + int(math.Round(r*math.Cos(φ)))
			y := station[1] + int(math.Round(r*math.Sin(φ)))
			fmt.Println(x*100 + y)
			return
		}
		vis[φ] = vis[φ][1:]
	}

	fmt.Printf("%dth vaporized asteroid not reached\n", TARGET)
}
