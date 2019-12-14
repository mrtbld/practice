package main

import (
	"fmt"
	"io/ioutil"
)

const (
	W = 25
	H = 6
)

type layer [H][W]rune
type image []layer
type counter map[rune]int

func readInput() string {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	return string(data)
}

func makeImage(data string) image {
	img := image{}
	l := layer{}
	var h, w int
	for _, r := range readInput() {
		l[h][w] = r
		w++
		if w < W {
			continue
		}
		w = 0
		h++
		if h < H {
			continue
		}
		h = 0
		img = append(img, l)
		l = layer{}
	}

	return img
}

func main() {
	var least counter
	for _, l := range makeImage(readInput()) {
		c := make(counter)
		for _, row := range l {
			for _, r := range row {
				c[r]++
			}
		}
		if least == nil || c['0'] < least['0'] {
			least = c
		}
	}

	fmt.Println(least['1'] * least['2'])
}
