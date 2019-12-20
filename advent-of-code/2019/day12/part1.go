package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

var bodyRe *regexp.Regexp

func init() {
	var err error
	bodyRe, err = regexp.Compile(`<x=(-?\d+), y=(-?\d+), z=(-?\d+)>`)
	if err != nil {
		panic(err)
	}
}

func mustAtoi(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic(err)
	}
	return i
}

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
}

type coord struct{ x, y, z int }

func (c coord) energy() int {
	return abs(c.x) + abs(c.y) + abs(c.z)
}

func (c coord) add(o coord) coord {
	return coord{
		x: c.x + o.x,
		y: c.y + o.y,
		z: c.z + o.z,
	}
}

func (c coord) neg() coord {
	return coord{
		x: -c.x,
		y: -c.y,
		z: -c.z,
	}
}

func (c coord) String() string {
	return fmt.Sprintf("(%d, %d, %d)", c.x, c.y, c.z)
}

func newBodyFromString(s string) (*body, error) {
	m := bodyRe.FindStringSubmatch(s)
	if len(m) == 0 {
		return nil, fmt.Errorf("can't create body from %q", s)
	}
	return &body{
		pos: coord{mustAtoi(m[1]), mustAtoi(m[2]), mustAtoi(m[3])},
	}, nil
}

type body struct {
	pos      coord
	velocity coord
}

func (b body) energy() int {
	return b.pos.energy() * b.velocity.energy()
}

func (b body) gravity(o body) coord {
	g := coord{}
	if b.pos.x > o.pos.x {
		g.x = -1
	} else if b.pos.x < o.pos.x {
		g.x = 1
	}
	if b.pos.y > o.pos.y {
		g.y = -1
	} else if b.pos.y < o.pos.y {
		g.y = 1
	}
	if b.pos.z > o.pos.z {
		g.z = -1
	} else if b.pos.z < o.pos.z {
		g.z = 1
	}
	return g
}

func (b *body) updateVelocity(c coord) {
	b.velocity = b.velocity.add(c)
}

func (b *body) advance() {
	b.pos = b.pos.add(b.velocity)
}

func (b body) String() string {
	return fmt.Sprintf("pos%s vel%s)", b.pos, b.velocity)
}

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	bodies := []*body{}
	for _, l := range strings.Split(string(data), "\n") {
		body, err := newBodyFromString(l)
		if err != nil {
			continue
		}
		bodies = append(bodies, body)
	}

	for i := 0; i < 1000; i++ {
		for j, a := range bodies {
			for k := j + 1; k < len(bodies); k++ {
				b := bodies[k]
				g := a.gravity(*b)
				a.updateVelocity(g)
				b.updateVelocity(g.neg())
			}
		}
		for _, b := range bodies {
			b.advance()
		}
	}

	energy := 0
	for _, b := range bodies {
		energy += b.energy()
	}

	fmt.Println(energy)
}
