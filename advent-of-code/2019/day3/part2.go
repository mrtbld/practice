package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
}

type move struct {
	dir  string
	dist int
}

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rawWirepaths := strings.Split(strings.TrimSpace(string(data)), "\n")
	wirepaths := make([][]move, len(rawWirepaths))

	for i, wirepath := range rawWirepaths {
		for _, piece := range strings.Split(wirepath, ",") {
			piece := strings.TrimSpace(piece)
			if piece == "" {
				continue
			}

			dist, err := strconv.Atoi(piece[1:])
			if err != nil {
				panic(err)
			}

			wirepaths[i] = append(wirepaths[i], move{
				dir:  string(piece[0]),
				dist: dist,
			})
		}
	}

	// (0, 0) is (left, top).
	var grid = make([]map[[2]int]int, len(wirepaths))

	for i, wirepath := range wirepaths {
		wiregrid := make(map[[2]int]int)
		d, x, y := 0, 0, 0
		for _, m := range wirepath {
			var dx, dy int
			switch m.dir {
			case "R":
				dx = 1
			case "D":
				dy = 1
			case "L":
				dx = -1
			case "U":
				dy = -1
			default:
				panic(fmt.Sprintf("unknown direction %q", m.dir))
			}
			for j := m.dist; j > 0; j-- {
				x, y = x+dx, y+dy
				p := [2]int{x, y}
				d += 1
				if wiregrid[p] == 0 {
					wiregrid[p] = d
				}
			}
		}
		grid[i] = wiregrid
	}

	var dist int
	var closest [2]int
	for p, da := range grid[0] {
		if db, ok := grid[1][p]; ok {
			if dist == 0 || da+db < dist {
				dist = da + db
				closest = p
			}
		}
	}

	fmt.Println("closest intersection", closest, "at distance", dist)
}
