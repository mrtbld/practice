package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

var moonRe *regexp.Regexp

func init() {
	var err error
	moonRe, err = regexp.Compile(`<x=(-?\d+), y=(-?\d+), z=(-?\d+)>`)
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

type coord struct{ x, y, z int }

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

func newMoonFromString(s string) (*moon, error) {
	m := moonRe.FindStringSubmatch(s)
	if len(m) == 0 {
		return nil, fmt.Errorf("can't create moon from %q", s)
	}
	return &moon{
		pos: coord{mustAtoi(m[1]), mustAtoi(m[2]), mustAtoi(m[3])},
	}, nil
}

type moon struct {
	pos      coord
	velocity coord
}

func (m moon) gravity(o moon) coord {
	g := coord{}
	if m.pos.x > o.pos.x {
		g.x = -1
	} else if m.pos.x < o.pos.x {
		g.x = 1
	}
	if m.pos.y > o.pos.y {
		g.y = -1
	} else if m.pos.y < o.pos.y {
		g.y = 1
	}
	if m.pos.z > o.pos.z {
		g.z = -1
	} else if m.pos.z < o.pos.z {
		g.z = 1
	}
	return g
}

func (m *moon) updateVelocity(c coord) {
	m.velocity = m.velocity.add(c)
}

func (m *moon) advance() {
	m.pos = m.pos.add(m.velocity)
}

func (m moon) String() string {
	return fmt.Sprintf("pos%s vel%s)", m.pos, m.velocity)
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	if a > b {
		a, b = b, a
	}
	return gcd(a, b-a)
}

func lcm(a, b int) int {
	return abs(a*b) / gcd(a, b)
}

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	moons := []*moon{}
	initial := []moon{}
	for _, l := range strings.Split(string(data), "\n") {
		moon, err := newMoonFromString(l)
		if err != nil {
			continue
		}
		moons = append(moons, moon)
		initial = append(initial, *moon)
	}

	var xc, yc, zc int
	for i := 0; xc == 0 || yc == 0 || zc == 0; i++ {
		for j, a := range moons {
			for k := j + 1; k < len(moons); k++ {
				b := moons[k]
				g := a.gravity(*b)
				a.updateVelocity(g)
				b.updateVelocity(g.neg())
			}
		}
		xCycles := xc == 0
		yCycles := yc == 0
		zCycles := zc == 0
		for j, a := range moons {
			a.advance()
			b := initial[j]
			xCycles = xCycles && a.pos.x == b.pos.x && a.velocity.x == b.velocity.x
			yCycles = yCycles && a.pos.y == b.pos.y && a.velocity.y == b.velocity.y
			zCycles = zCycles && a.pos.z == b.pos.z && a.velocity.z == b.velocity.z
		}
		if xCycles {
			xc = i + 1
		}
		if yCycles {
			yc = i + 1
		}
		if zCycles {
			zc = i + 1
		}
	}

	fmt.Println(lcm(lcm(xc, yc), zc))
}
