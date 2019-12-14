package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const (
	W = 25
	H = 6
)

type color int
type layer [H][W]color
type image []layer

const (
	TRANS color = iota
	BLACK
	WHITE
)

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
	for _, p := range readInput() {
		var c color
		switch p {
		case '0':
			c = BLACK
		case '1':
			c = WHITE
		case '2':
			c = TRANS
		}
		l[h][w] = c
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

func flatten(img image) layer {
	var flattened layer
	for _, l := range img {
		for h, row := range l {
			for w, c := range row {
				if flattened[h][w] == TRANS {
					flattened[h][w] = c
				}
			}
		}
	}

	return flattened
}

func render(img image) string {
	flattened := flatten(img)
	lines := make([]string, len(flattened))
	for h, row := range flattened {
		line := make([]string, len(row))
		for w, c := range row {
			if c == WHITE {
				line[w] = "█"
			} else {
				line[w] = " "
			}
		}
		lines[h] = strings.Join(line, "")
	}

	return strings.Join(lines, "\n")

}

func main() {
	fmt.Println(render(makeImage(readInput())))
}
