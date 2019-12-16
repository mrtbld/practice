package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const (
	instAdd = 1
	instMul = 2
	instIn  = 3
	instOut = 4
	instJIT = 5
	instJIF = 6
	instLT  = 7
	instEq  = 8
	instRB  = 9
	instEnd = 99

	modePos = 0
	modeVal = 1
	modeRel = 2
)

var done = errors.New("done")

type panel struct{ x, y int }

const (
	turnLeft = iota
	turnRight
)

var dirDeltas = [4]panel{
	{0, -1}, // up
	{1, 0},  // right
	{0, 1},  // down
	{-1, 0}, // left
}

func read(mem map[int]int, relbase int, modes [3]int, pos int, offset int) int {
	switch modes[offset-1] {
	case modePos:
		return mem[mem[pos+offset]]
	case modeVal:
		return mem[pos+offset]
	case modeRel:
		return mem[relbase+mem[pos+offset]]
	default:
		panic(fmt.Errorf("unknown mode %d", modes[offset-1]))
	}
}

func write(mem map[int]int, relbase int, modes [3]int, pos int, offset int, value int) {
	switch modes[offset-1] {
	case modePos:
		mem[mem[pos+offset]] = value
	case modeVal:
		panic(fmt.Errorf("value mode for write"))
	case modeRel:
		mem[relbase+mem[pos+offset]] = value
	default:
		panic(fmt.Errorf("unknown mode %d", modes[offset-1]))
	}
}

func run(intcodes []int, in chan int, out chan<- int, e chan<- error) {
	mem := make(map[int]int, len(intcodes))
	for i, v := range intcodes {
		mem[i] = v
	}

	var relbase int
	var modes [3]int
	var i int

	r := func(offset int) int {
		return read(mem, relbase, modes, i, offset)
	}

	w := func(offset int, value int) {
		write(mem, relbase, modes, i, offset, value)
	}

	for i = 0; i < len(mem); i++ {
		instruction := mem[i] % 100
		modes = [3]int{
			(mem[i] / 100) % 10,
			(mem[i] / 1000) % 10,
			(mem[i] / 10000) % 10,
		}

		switch instruction {
		case instAdd:
			w(3, r(1)+r(2))
			i += 3
		case instMul:
			w(3, r(1)*r(2))
			i += 3
		case instIn:
			in <- 0
			w(1, <-in)
			i += 1
		case instOut:
			out <- r(1)
			i += 1
		case instEnd:
			e <- done
			return
		case instJIT:
			if r(1) != 0 {
				i = r(2) - 1
			} else {
				i += 2
			}
		case instJIF:
			if r(1) == 0 {
				i = r(2) - 1
			} else {
				i += 2
			}
		case instLT:
			if r(1) < r(2) {
				w(3, 1)
			} else {
				w(3, 0)
			}
			i += 3
		case instEq:
			if r(1) == r(2) {
				w(3, 1)
			} else {
				w(3, 0)
			}
			i += 3
		case instRB:
			relbase += r(1)
			i += 1
		default:
			e <- fmt.Errorf("not a valid instruction at position %d: %d", i, mem[i])
			return
		}
	}
	e <- fmt.Errorf("halt instruction not found")
}

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rawIntcodes := strings.Split(string(data), ",")
	intcodes := make([]int, len(rawIntcodes))
	for i, v := range rawIntcodes {
		var err error
		intcodes[i], err = strconv.Atoi(strings.TrimSpace(v))
		if err != nil {
			panic(err)
		}
	}

	in := make(chan int)
	out := make(chan int)
	e := make(chan error)
	go run(intcodes, in, out, e)

	var panels = map[panel]int{}
	var pos panel
	var dir int
	var isDone, outIsDir bool
	for !isDone {
		select {
		case <-in:
			in <- panels[pos]
		case v := <-out:
			if outIsDir {
				switch v {
				case turnLeft:
					dir = (dir + 3) % 4
				case turnRight:
					dir = (dir + 1) % 4
				default:
					panic(fmt.Errorf("unknown direction %d", v))
				}
				pos.x += dirDeltas[dir].x
				pos.y += dirDeltas[dir].y
			} else {
				panels[pos] = v
			}
			outIsDir = !outIsDir
		case err := <-e:
			if !errors.Is(err, done) {
				panic(err)
			}
			isDone = true
		}
	}

	fmt.Println(len(panels))
}
